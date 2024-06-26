from django.db import models
from django.conf import settings

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    player_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.position} {self.player_number}"
    
    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    place = models.SmallIntegerField(null=True)
    total_points = models.SmallIntegerField(null=True)
    capitan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    players = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Drużyna'
        verbose_name_plural = 'Drużyny'

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wydział'
        verbose_name_plural = 'Wydziały'


