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
    players = models.ManyToManyField(Player)

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

class UserTeam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    team = models.ForeignKey('Team', on_delete=models.PROTECT)
    is_capitan = models.BooleanField()

    def __str__(self):
        if self.is_capitan:
            return f"{self.user}-{self.team} Kapitan"
        return f"{self.user}-{self.team}"

    class Meta:
        verbose_name = 'Kapitan'
        verbose_name_plural = 'Kapitanowie'

