from django.contrib import admin
from .models.match_ranking import Match, GlobalRanking, SportRanking
from .models.sport_edition import Sport, Edition, SportGlobalPoints
from .models.team_department import Team, Department, UserTeam

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    exclude = ['winner_team']

@admin.register(GlobalRanking)
class GlobalRankingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    pass

@admin.register(SportGlobalPoints)
class SportGlobalPointsAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    exclude = ('place', 'total_points')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(UserTeam)
class UserTeamAdmin(admin.ModelAdmin):
    pass

@admin.register(SportRanking)
class UserTeamAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
