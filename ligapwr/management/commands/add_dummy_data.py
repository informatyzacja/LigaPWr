from django.core.management.base import BaseCommand, CommandError
from ...models import Sport, Edition, SportGlobalPoints, Team, Department, Match

class Command(BaseCommand):
    help = "Add dummy data to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sport1, _ = Sport.objects.get_or_create(name='Piłka nożna', win_points=3, draw_points=1, lose_points=0)
        sport2, _ = Sport.objects.get_or_create(name='Koszykówka', win_points=2, draw_points=1, lose_points=0)
        sport3, _ = Sport.objects.get_or_create(name='Siatkówka', win_points=2, draw_points=1, lose_points=0)

        edition, _ = Edition.objects.get_or_create(name='Lato 2024')

        SportGlobalPoints.objects.get_or_create(sport=sport1, edition=edition, 
            first_place_points=10, second_place_points=5, third_place_points=3, fourth_place_points=1, other_places_points=0
        )
        SportGlobalPoints.objects.get_or_create(sport=sport2, edition=edition, 
            first_place_points=10, second_place_points=5, third_place_points=3, fourth_place_points=1, other_places_points=0
        )
        SportGlobalPoints.objects.get_or_create(sport=sport3, edition=edition, 
            first_place_points=10, second_place_points=5, third_place_points=3, fourth_place_points=1, other_places_points=0
        )


        department1, _ = Department.objects.get_or_create(name='W1')
        department2, _ = Department.objects.get_or_create(name='W2')
        department3, _ = Department.objects.get_or_create(name='W3')


        teamA, _ = Team.objects.get_or_create(name='Zespół A', department=department1, sport=sport1, edition=edition)
        teamB, _ = Team.objects.get_or_create(name='Zespół B', department=department1, sport=sport2, edition=edition)
        teamC, _ = Team.objects.get_or_create(name='Zespół C', department=department1, sport=sport3, edition=edition)

        teamD, _ = Team.objects.get_or_create(name='Zespół D', department=department2, sport=sport1, edition=edition)
        teamE, _ = Team.objects.get_or_create(name='Zespół E', department=department2, sport=sport2, edition=edition)
        teamF, _ = Team.objects.get_or_create(name='Zespół F', department=department2, sport=sport3, edition=edition)

        teamG, _ = Team.objects.get_or_create(name='Zespół G', department=department3, sport=sport1, edition=edition)
        teamH, _ = Team.objects.get_or_create(name='Zespół H', department=department3, sport=sport2, edition=edition)
        teamI, _ = Team.objects.get_or_create(name='Zespół I', department=department3, sport=sport3, edition=edition)


        match1 = Match.objects.get_or_create(team_one=teamA, team_two=teamD, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match2 = Match.objects.get_or_create(team_one=teamB, team_two=teamE, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match3 = Match.objects.get_or_create(team_one=teamC, team_two=teamF, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match4 = Match.objects.get_or_create(team_one=teamA, team_two=teamG, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match5 = Match.objects.get_or_create(team_one=teamB, team_two=teamH, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match6 = Match.objects.get_or_create(team_one=teamC, team_two=teamI, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match7 = Match.objects.get_or_create(team_one=teamD, team_two=teamG, start_time='2024-05-10 20:50', end_time='2024-05-10 22:50')
        match8 = Match.objects.get_or_create(team_one=teamE, team_two=teamH, start_time='2024-05-10 20:50', end_time='2024-05-10 22:50')
        match9 = Match.objects.get_or_create(team_one=teamF, team_two=teamI, start_time='2024-05-10 20:50', end_time='2024-05-10 22:50')

        from ligapwr.models import calculate_all_points
        calculate_all_points()

        print ("Dummy data added")

        
