from django.shortcuts import render
from django.utils import timezone
from ligapwr.models.match_ranking import Match

# Create your views here.
def schedule(request):
    # Showing only future matches
    matches_for_schedule = Match.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'ligapwr/schedule.html', {'mecze':matches_for_schedule})

def standings(request):
    return render(request, 'ligapwr/standings.html')

def history(request):
    matches_for_history = Match.objects.filter(start_time__lt=timezone.now()).order_by('start_time')
    return render(request, 'ligapwr/history.html', {'mecze':matches_for_history})

