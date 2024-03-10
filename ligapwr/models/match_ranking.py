from django.db import models
from django.conf import settings
from django.db.models import Q
from django import forms


class Match(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    team_one = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_one')
    team_two = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='team_two')
    referee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    score_team_one = models.SmallIntegerField(null=True)
    score_team_two = models.SmallIntegerField(null=True)
    winner_team = models.ForeignKey('Team', on_delete=models.PROTECT, related_name='winner_team', null=True)

    def __str__(self):
        return f"{self.team_one}-{self.team_two}-{self.start_time}"

    class Meta:
        verbose_name = 'Mecz'
        verbose_name_plural = 'Mecze'

    def save(self, *args, **kwargs):
        if self.score_team_one > self.score_team_two:
            self.winner_team = self.team_one
        elif self.score_team_one < self.score_team_two:
            self.winner_team = self.team_two
        else:
            self.winner_team = None

        super(Match, self).save(*args, **kwargs)
        SportRanking.calculate_points(SportRanking, self.team_one.sport, self.team_one.edition)

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

    def calculate_points(self, edition):
        # Calculate the points
        from . import Department, SportRanking, SportGlobalPoints
        for department in Department.objects.all():
            raking, _ = self.objects.get_or_create(edition=edition, department=department, defaults={'place': 0, 'total_points': 0})
            raking.total_points = 0
            
            sport_ranking = SportRanking.objects.filter(edition=edition, team__department=department).order_by('place')
            calculated_departments = []
            
            for ranking in sport_ranking:
                if ranking.team.department in calculated_departments:
                    continue
                calculated_departments.append(ranking.team.department)

                global_points = SportGlobalPoints.objects.get(sport=ranking.sport, edition=edition)
                if ranking.place_for_department == 1:
                    raking.total_points += global_points.first_place_points
                elif ranking.place_for_department == 2:
                    raking.total_points += global_points.second_place_points
                elif ranking.place_for_department == 3:
                    raking.total_points += global_points.third_place_points
                elif ranking.place_for_department == 4:
                    raking.total_points += global_points.fourth_place_points
                else:
                    raking.total_points += global_points.other_places_points

            raking.save()

        # Update the places
        GlobalRanking.update_places(GlobalRanking, edition)

    def update_places(self, edition):
        # Update the places
        rankings = GlobalRanking.objects.filter(edition=edition).order_by('-total_points')
        place = 1
        for ranking in rankings:
            ranking.place = place
            ranking.save()
            place += 1

class SportRanking(models.Model):
    team = models.ForeignKey('Team', on_delete=models.PROTECT)
    place = models.SmallIntegerField()
    place_for_department = models.SmallIntegerField()
    total_points = models.SmallIntegerField()
    edition = models.ForeignKey('Edition', on_delete=models.PROTECT)
    sport = models.ForeignKey('Sport', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.sport}-{self.edition}"
    
    class Meta:
        verbose_name = 'Raking sportu'
        verbose_name_plural = 'Ranking sportu'

    def calculate_points(self, sport, edition):
        # Calculate the points
        from . import Team
        for team in Team.objects.filter(sport=sport, edition=edition):
            raking, _ = SportRanking.objects.get_or_create(edition=edition, sport=sport, team=team, defaults={'place': 0, 'place_for_department': 0, 'total_points': 0})
            raking.total_points = 0
            matches = Match.objects.filter(Q(team_one=team) | Q(team_two=team))

            for match in matches:
                if match.winner_team == team:
                    raking.total_points += sport.win_points
                elif match.score_team_one == match.score_team_two:
                    raking.total_points += sport.draw_points
                elif match.winner_team:
                    raking.total_points += sport.lose_points

            raking.save()

        # Update the places
        SportRanking.update_places(SportRanking, sport, edition)


    def update_places(self, sport, edition):
        # Update the places
        rankings = SportRanking.objects.filter(edition=edition, sport=sport).order_by('-total_points')
        place = 1
        for ranking in rankings:
            ranking.place = place
            ranking.save()
            place += 1

        # Update the places for department
        place = 1
        calculated_departments = []
        rankings = SportRanking.objects.filter(edition=edition, sport=sport).order_by('-total_points')
        for ranking in rankings:
            if ranking.team.department not in calculated_departments:
                calculated_departments.append(ranking.team.department)
                ranking.place_for_department = place
                place += 1
            else:
                ranking.place_for_department = 0
            ranking.save()


        GlobalRanking.calculate_points(GlobalRanking, edition)