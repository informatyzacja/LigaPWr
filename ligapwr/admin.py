from django.contrib import admin
from .models.match_ranking import Match, GlobalRanking, SportRanking
from .models.sport_edition import Sport, Edition, SportGlobalPoints
from .models.team_department import Player, Team, Department

from django import forms
class MatchAdminForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['team_one'] == cleaned_data['team_two']:
            raise forms.ValidationError('Drużyny nie mogą być takie same')
        
        if cleaned_data['team_one'].sport != cleaned_data['team_two'].sport:
            raise forms.ValidationError('Drużyny muszą być tego samego sportu')
        
        if cleaned_data['start_time'] > cleaned_data['end_time']:
            raise forms.ValidationError('Data zakończenia nie może być wcześniejsza niż data rozpoczęcia')
        
        if cleaned_data['team_one'].edition != cleaned_data['team_two'].edition:
            raise forms.ValidationError('Drużyny muszą być z tej samej edycji')

        return cleaned_data
    
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    form = MatchAdminForm
    list_display = ('team_one', 'team_two', 'start_time', 'end_time', 'winner_team')
    exclude = ['winner_team']

@admin.register(GlobalRanking)
class GlobalRankingAdmin(admin.ModelAdmin):
    list_display = ('department', 'place', 'total_points', 'edition')
    list_filter = ('edition', 'department')
    ordering = ('edition', 'place')

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
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
    list_display = ('name', 'department', 'sport', 'edition')
    exclude = ('place', 'total_points')
    list_filter = ('department', 'sport', 'edition')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(SportRanking)
class SportRankingAdmin(admin.ModelAdmin):
    list_display = ('team', 'place', 'place_for_department', 'total_points', 'edition', 'sport')
    list_filter = ('edition', 'sport')

    ordering = ('edition', 'sport', 'place')

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
