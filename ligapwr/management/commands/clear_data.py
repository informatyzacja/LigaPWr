from django.core.management.base import BaseCommand, CommandError
from ...models import Sport, Edition, SportGlobalPoints, Team, Department, Match, SportRanking, GlobalRanking

class Command(BaseCommand):
    help = "Clear data from the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Match.objects.all().delete()
        SportRanking.objects.all().delete()
        Team.objects.all().delete()
        SportGlobalPoints.objects.all().delete()
        Sport.objects.all().delete()
        GlobalRanking.objects.all().delete()
        Department.objects.all().delete()
        Edition.objects.all().delete()

        print("Data cleared successfully")


        
