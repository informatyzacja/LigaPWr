from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    total_points = models.SmallIntegerField()

class Department(models.Model):
    name = models.CharField(max_length=100)

class UserTeam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    team = models.ForeignKey('Team', on_delete=models.PROTECT)
    is_capitan = models.BooleanField()
