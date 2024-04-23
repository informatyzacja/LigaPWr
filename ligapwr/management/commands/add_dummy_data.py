from django.core.management.base import BaseCommand, CommandError
from ...models import Sport, Edition, SportGlobalPoints, Team, Department, Match

class Command(BaseCommand):
    help = "Add dummy data to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sport1, _ = Sport.objects.get_or_create(name='Piłka nożna', win_points=3, draw_points=1, lose_points=0, emoji='⚽')
        sport2, _ = Sport.objects.get_or_create(name='Koszykówka', win_points=2, draw_points=1, lose_points=0, emoji='🏀')
        sport3, _ = Sport.objects.get_or_create(name='Siatkówka', win_points=2, draw_points=1, lose_points=0, emoji='🏐')

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
        department4, _ = Department.objects.get_or_create(name='W4')
        department5, _ = Department.objects.get_or_create(name='W5')
        department6, _ = Department.objects.get_or_create(name='W6')
        department7, _ = Department.objects.get_or_create(name='W7')
        department8, _ = Department.objects.get_or_create(name='W8')
        department9, _ = Department.objects.get_or_create(name='W9')
        department10, _ = Department.objects.get_or_create(name='W10')
        department11, _ = Department.objects.get_or_create(name='W11')
        department12, _ = Department.objects.get_or_create(name='W12')
        department13, _ = Department.objects.get_or_create(name='W13')
        department14, _ = Department.objects.get_or_create(name='W14')
        department15, _ = Department.objects.get_or_create(name='W15')
        department16, _ = Department.objects.get_or_create(name='W16')
        department17, _ = Department.objects.get_or_create(name='W17')
        department18, _ = Department.objects.get_or_create(name='W18')
        department19, _ = Department.objects.get_or_create(name='W19')
        department20, _ = Department.objects.get_or_create(name='W20')
        department21, _ = Department.objects.get_or_create(name='W21')
        department22, _ = Department.objects.get_or_create(name='W22')
        department23, _ = Department.objects.get_or_create(name='W23')
        department24, _ = Department.objects.get_or_create(name='W24')
        department25, _ = Department.objects.get_or_create(name='W25')



        teamA, _ = Team.objects.get_or_create(name='Zespół A', department=department1, sport=sport1, edition=edition)
        teamB, _ = Team.objects.get_or_create(name='Zespół B', department=department1, sport=sport2, edition=edition)
        teamC, _ = Team.objects.get_or_create(name='Zespół C', department=department1, sport=sport3, edition=edition)

        teamD, _ = Team.objects.get_or_create(name='Zespół D', department=department2, sport=sport1, edition=edition)
        teamE, _ = Team.objects.get_or_create(name='Zespół E', department=department2, sport=sport2, edition=edition)
        teamF, _ = Team.objects.get_or_create(name='Zespół F', department=department2, sport=sport3, edition=edition)

        teamG, _ = Team.objects.get_or_create(name='Zespół G', department=department3, sport=sport1, edition=edition)
        teamH, _ = Team.objects.get_or_create(name='Zespół H', department=department3, sport=sport2, edition=edition)
        teamI, _ = Team.objects.get_or_create(name='Zespół I', department=department3, sport=sport3, edition=edition)

        teamJ, _ = Team.objects.get_or_create(name='Zespół J', department=department1, sport=sport1, edition=edition)
        teamK, _ = Team.objects.get_or_create(name='Zespół K', department=department1, sport=sport2, edition=edition)
        teamL, _ = Team.objects.get_or_create(name='Zespół L', department=department1, sport=sport3, edition=edition)

        teamM, _ = Team.objects.get_or_create(name='Zespół M', department=department2, sport=sport1, edition=edition)
        teamN, _ = Team.objects.get_or_create(name='Zespół N', department=department2, sport=sport2, edition=edition)
        teamO, _ = Team.objects.get_or_create(name='Zespół O', department=department2, sport=sport3, edition=edition)

        teamP, _ = Team.objects.get_or_create(name='Zespół P', department=department3, sport=sport1, edition=edition)
        teamR, _ = Team.objects.get_or_create(name='Zespół R', department=department3, sport=sport2, edition=edition)
        teamS, _ = Team.objects.get_or_create(name='Zespół S', department=department3, sport=sport3, edition=edition)
        
        teamT, _ = Team.objects.get_or_create(name='Zespół J', department=department1, sport=sport1, edition=edition)
        teamU, _ = Team.objects.get_or_create(name='Zespół K', department=department1, sport=sport2, edition=edition)
        teamW, _ = Team.objects.get_or_create(name='Zespół L', department=department1, sport=sport3, edition=edition)

        teamYY, _ = Team.objects.get_or_create(name='Zespół M', department=department2, sport=sport1, edition=edition)
        teamAA, _ = Team.objects.get_or_create(name='Zespół N', department=department2, sport=sport2, edition=edition)
        teamBB, _ = Team.objects.get_or_create(name='Zespół O', department=department2, sport=sport3, edition=edition)

        teamCC, _ = Team.objects.get_or_create(name='Zespół P', department=department3, sport=sport1, edition=edition)
        teamDD, _ = Team.objects.get_or_create(name='Zespół R', department=department3, sport=sport2, edition=edition)
        teamEE, _ = Team.objects.get_or_create(name='Zespół S', department=department3, sport=sport3, edition=edition)

        teamX,  _ = Team.objects.get_or_create(name='Zespół X' , department=department1, sport=sport2, edition=edition)
        teamX1, _ = Team.objects.get_or_create(name='Zespół X1', department=department1, sport=sport2, edition=edition)


        match1, _ = Match.objects.get_or_create(team_one=teamA, team_two=teamD, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match2, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamE, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match3, _= Match.objects.get_or_create(team_one=teamC, team_two=teamF, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match4, _ = Match.objects.get_or_create(team_one=teamA, team_two=teamG, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match5, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamH, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match6, _= Match.objects.get_or_create(team_one=teamC, team_two=teamI, start_time='2024-03-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match7, _ = Match.objects.get_or_create(team_one=teamD, team_two=teamG, start_time='2024-05-10 20:50', end_time='2024-05-10 22:50')
        match8, _ = Match.objects.get_or_create(team_one=teamF, team_two=teamI, start_time='2024-05-10 20:50', end_time='2024-05-10 22:50')


        match9, _ = Match.objects.get_or_create(team_one=teamD, team_two=teamG, start_time='2024-06-10 20:50', end_time='2024-06-10 22:50')
        match10, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamH, start_time='2024-06-10 20:50', end_time='2024-06-10 22:50')


        match11, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamH, start_time='2024-04-10 14:50', end_time='2024-04-10 16:50', score_team_one=1, score_team_two=0)
        match12, _ = Match.objects.get_or_create(team_one=teamF, team_two=teamI, start_time='2024-04-10 20:50', end_time='2024-04-10 22:50', score_team_one=3, score_team_two=1)

        match13, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamX , start_time='2024-04-10 20:50', end_time='2024-04-10 22:50', score_team_one=1, score_team_two=0)
        match14, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamX1, start_time='2024-04-10 20:50', end_time='2024-04-10 22:50', score_team_one=2, score_team_two=2)

        match15, _ = Match.objects.get_or_create(team_one=teamA, team_two=teamD, start_time='2024-07-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match16, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamE, start_time='2024-07-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match17, _= Match.objects.get_or_create(team_one=teamC, team_two=teamF, start_time='2024-07-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match18, _ = Match.objects.get_or_create(team_one=teamA, team_two=teamG, start_time='2024-08-10 20:50', end_time='2024-03-10 22:50', score_team_one=1, score_team_two=0)
        match19, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamH, start_time='2024-08-10 20:50', end_time='2024-03-10 22:50', score_team_one=2, score_team_two=2)
        match20, _= Match.objects.get_or_create(team_one=teamC, team_two=teamI, start_time='2024-08-10 20:50', end_time='2024-03-10 22:50', score_team_one=3, score_team_two=1)

        match21, _ = Match.objects.get_or_create(team_one=teamD, team_two=teamG, start_time='2024-09-10 20:50', end_time='2024-05-10 22:50')
        match22, _ = Match.objects.get_or_create(team_one=teamF, team_two=teamI, start_time='2024-09-10 20:50', end_time='2024-05-10 22:50')


        match23, _ = Match.objects.get_or_create(team_one=teamD, team_two=teamG, start_time='2024-10-10 20:50', end_time='2024-06-10 22:50')
        match24, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamH, start_time='2024-10-10 20:50', end_time='2024-06-10 22:50')


        match25, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamH, start_time='2024-11-10 14:50', end_time='2024-04-10 16:50', score_team_one=1, score_team_two=0)
        match26, _ = Match.objects.get_or_create(team_one=teamF, team_two=teamI, start_time='2024-11-10 20:50', end_time='2024-04-10 22:50', score_team_one=3, score_team_two=1)

        match27, _ = Match.objects.get_or_create(team_one=teamE, team_two=teamX , start_time='2024-12-10 20:50', end_time='2024-04-10 22:50', score_team_one=1, score_team_two=0)
        match28, _ = Match.objects.get_or_create(team_one=teamB, team_two=teamX1, start_time='2024-12-10 20:50', end_time='2024-04-10 22:50', score_team_one=2, score_team_two=2)

        from ligapwr.models import calculate_all_points
        calculate_all_points()

        print ("Dummy data added")

        
