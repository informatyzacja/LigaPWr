from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    win_points = models.SmallIntegerField()
    draw_points = models.SmallIntegerField()
    lose_points = models.SmallIntegerField()
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
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
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    first_place_points = models.SmallIntegerField()
    second_place_points = models.SmallIntegerField(default=0)
    third_place_points = models.SmallIntegerField(default=0)
    fourth_place_points = models.SmallIntegerField(default=0)
    other_places_points = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.sport.name} - {self.edition.name}'

    class Meta:
        verbose_name = 'Punkty globalne'
        verbose_name_plural = 'Punkty globalne'