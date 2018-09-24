from django.urls import path

from . import views

app_name = "clubs"
urlpatterns = [
    # splash page
    path('', views.home, name='home'),
    # returns list of clubs in JSON format 
    path('api/clubs/', views.clubs, name='clubs'),
    # returns the current user's rankings
    path('api/rankings/', views.yourrankings, name='yourrankings'),
    # page for creating a new club
    path('create/', views.create, name='create'),
    # page for ranking clubs
    path('rank/', views.rank, name='rank'),
    # signup page
    path('signup/', views.SignUp.as_view(), name='signup'),
]