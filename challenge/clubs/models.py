from django.db import models
from django.contrib.auth.models import AbstractUser

class Club(models.Model):
    name = models.CharField(max_length=200, unique=True)
    size = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class User(AbstractUser):
    YEAR_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    )
    SCHOOL_CHOICES = (
    ('EAS', 'Engineering'),
    ('SAS', 'College'),
    ('WHA', 'Wharton'),
    ('NUR', 'Nursing'),
    ('GRD', 'Graduate'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    school = models.CharField(max_length=3, choices=SCHOOL_CHOICES)
    def __str__(self):
        return self.email

# model representing a user's ranking of a club
class Ranking(models.Model):
    user = models.ForeignKey(User, on_delete="PROTECT")
    club = models.ForeignKey(Club, on_delete="PROTECT")
    rank = models.IntegerField()
    def __str__(self):
        return self.club.name
