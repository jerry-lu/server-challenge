from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Club, Ranking

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'year', 'school')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'year', 'school')


class ClubCreationForm(ModelForm):

    class Meta:
        model = Club
        fields = ('name', 'size')

class ClubRankingForm(ModelForm):
    for club in Club.objects.all():
        class Meta:
            model = Ranking
            fields = ('club', 'rank')