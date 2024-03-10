from django.db import models
from django.conf import settings

class Match(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    team_one = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_one')
    team_two = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_two')
    referee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    score_team_one = models.SmallIntegerField(null=True)
    score_team_two = models.SmallIntegerField(null=True)
    winner_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='winner_team', null=True)

    def __str__(self):
        return f"{self.team_one}-{self.team_two}-{self.start_time}"

    class Meta:
        verbose_name = 'Mecz'
        verbose_name_plural = 'Mecze'

class GlobalRanking(models.Model):
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    total_points = models.SmallIntegerField()
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)

    def __str__(self):
        return f"Ranking globalny edycja {self.edition}"
    
    class Meta:
        verbose_name = 'Ranking globalny'
        verbose_name_plural = 'Ranking Globalny'

class SportRanking(models.Model):
    team = models.ForeignKey('Team', on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    total_points = models.SmallIntegerField()
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.sport}-{self.edition}"
    
    class Meta:
        verbose_name = 'Raking sportu'
        verbose_name_plural = 'Ranking sportu'