from typing import Iterable
from django.db import models

from . import SportRanking, GlobalRanking

def calculate_all_points():
    for sport in Sport.objects.all():
        sport.save()

class Sport(models.Model):
    name = models.CharField(max_length=100)
    win_points = models.SmallIntegerField()
    draw_points = models.SmallIntegerField()
    lose_points = models.SmallIntegerField()
    archive = models.BooleanField(default=False)
    emoji = models.CharField(max_length=2, default='🏆')

    def __str__(self):
        return self.name
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        saved = super().save()
        for edition in Edition.objects.all():
            SportRanking.calculate_points(self, edition)
        return saved

    
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sporty'

class Edition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Edycja'
        verbose_name_plural = 'Edycje'

class SportGlobalPoints(models.Model):
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE)
    first_place_points = models.SmallIntegerField()
    second_place_points = models.SmallIntegerField(default=0)
    third_place_points = models.SmallIntegerField(default=0)
    fourth_place_points = models.SmallIntegerField(default=0)
    other_places_points = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.sport.name} - {self.edition.name}'
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        saved = super().save()
        GlobalRanking.calculate_points(self.edition)
        return saved

    class Meta:
        verbose_name = 'Punkty globalne'
        verbose_name_plural = 'Punkty globalne'