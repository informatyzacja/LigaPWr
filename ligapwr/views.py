from django.shortcuts import render

# Create your views here.
def schedule(request):
    return render(request, 'ligapwr/schedule.html')

def standings(request):
    return render(request, 'ligapwr/standings.html')

def history(request):
    return render(request, 'ligapwr/history.html')

