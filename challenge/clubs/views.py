from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import CustomUserCreationForm, ClubCreationForm, ClubRankingForm
from .models import Club, Ranking


# home page for pcr
def home(request):
    clubs = Club.objects.all()
    return render(request, "home.html", {"clubs": clubs})

# page with the form for ranking clubs. Also displays your current ranking
def rank(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClubRankingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('/clubs/api/rankings')
    else :
        ranks = Ranking.objects.filter(user=request.user).order_by('rank')  
        clubs = Club.objects.all()
        form = ClubRankingForm()
        return render(request, "rankings.html", {'ranks': ranks, 'clubs': clubs, 'form': form})

# displays clubs in json format
@csrf_exempt
def clubs(request):
    data = serializers.serialize('json', Club.objects.all())
    return JsonResponse(data, safe = False)

# displays current user's ranking in json format
@csrf_exempt
def yourrankings(request):
    data = serializers.serialize('json', Ranking.objects.filter(user=request.user))
    return JsonResponse(data, safe = False)

# form for creating a new club
def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClubCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/clubs/api/clubs')
    else :  
        form = ClubCreationForm()
        return render(request, 'create.html', {'form': form})

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'    
