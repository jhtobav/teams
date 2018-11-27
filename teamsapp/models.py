from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Member(models.Model):
    teams = models.ManyToManyField(Team)
    email = models.CharField(max_length=128)
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return "{}-{}".format(self.teams.all(), self.full_name)

