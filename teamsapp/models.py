from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateField(default=timezone.now)


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete='cascade')
    user_id = models.CharField(max_length=50)

