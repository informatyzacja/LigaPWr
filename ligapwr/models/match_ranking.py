from django.db import models
from django.conf import settings

class Match(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    team_one = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_one')
    team_two = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_two')
    referee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    score_team_one = models.SmallIntegerField()
    score_team_two = models.SmallIntegerField()
    winner_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='winner_team')

class GlobalRanking(models.Model):
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    total_points = models.SmallIntegerField()
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)

