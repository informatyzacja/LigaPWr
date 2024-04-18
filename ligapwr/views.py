from django.shortcuts import render
from django.utils import timezone
from ligapwr.models import Match, SportRanking, GlobalRanking, Sport, Team, Department
from django.db import models

def get_sports():
    return Sport.objects.all()

def get_departments():
    return Department.objects.all()

# Create your views here.
def schedule(request):
    # Showing only future matches
    matches_for_schedule = Match.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    if request.GET.get('sport'):
        matches_for_schedule = matches_for_schedule.filter(team_one__sport__id=request.GET.get('sport'))

    days = matches_for_schedule.values_list('start_time__date', flat=True).distinct()
    
    matches_list = {}
    for day in days:
        matches_list[day] = matches_for_schedule.filter(start_time__date=day)


    return render(request, 'ligapwr/schedule.html', {'mecze':matches_list, 'sports': get_sports()})

def standings(request):
    # TODO: Wybór sportu i global rankingu
    if request.GET.get('sport'):
        sport_ranking = SportRanking.objects.filter(sport__id=request.GET.get('sport')).order_by('place')
        return render(request, 'ligapwr/standings.html', { 'sport_ranking': sport_ranking, 'sports': get_sports() })
    else:
        global_ranking = GlobalRanking.objects.all().order_by('place')
        return render(request, 'ligapwr/global_standings.html', { 'global_ranking': global_ranking, 'sports': get_sports() })


def history(request):
    matches_for_history = Match.objects.filter(start_time__lt=timezone.now()).order_by('start_time')

    if request.GET.get('sport'):
        matches_for_history = matches_for_history.filter(team_one__sport__id=request.GET.get('sport'))

    days = matches_for_history.values_list('start_time__date', flat=True).distinct()
    
    matches_list = {}
    for day in days:
        matches_list[day] = matches_for_history.filter(start_time__date=day)


    return render(request, 'ligapwr/history.html', {'mecze':matches_list, 'sports': get_sports() })

def teams(request):
    teams = Team.objects.order_by('sport', 'department')

    if request.GET.get('sport'):
        teams = teams.filter(sport__id=request.GET.get('sport'))

    if request.GET.get('department'):
        teams = teams.filter(department__id=request.GET.get('department'))
        
    return render(request, 'ligapwr/teams.html', {'teams': teams, 'sports': get_sports(), 'departments': get_departments(), 'request': request})