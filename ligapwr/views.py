from django.shortcuts import render
from django.utils import timezone
from ligapwr.models import Match, SportRanking, GlobalRanking, Sport
from django.db import models

# Create your views here.
def schedule(request):
    # Showing only future matches
    matches_for_schedule = Match.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'ligapwr/schedule.html', {'mecze':matches_for_schedule})

def standings(request):
    # TODO: Wybór sportu i global rankingu
    sport_ranking = SportRanking.objects.filter(sport=Sport.objects.first()).order_by('place')
    # global_ranking = GlobalRanking.objects.filter()

    return render(request, 'ligapwr/standings.html', { 'sport_ranking': sport_ranking })

def history(request):
    matches_for_history = Match.objects.filter(start_time__lt=timezone.now()).order_by('start_time')
    return render(request, 'ligapwr/history.html', {'mecze':matches_for_history})

