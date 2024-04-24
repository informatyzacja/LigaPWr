from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from ligapwr.models.team_department import Player
from ...models import Sport, Edition, SportGlobalPoints, Team, Department, Match


class Command(BaseCommand):
    help = "Add dummy data to the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sport1, _ = Sport.objects.get_or_create(name='Piłka nożna', win_points=3, draw_points=1, lose_points=0, emoji='⚽')
        sport2, _ = Sport.objects.get_or_create(name='Koszykówka', win_points=2, draw_points=1, lose_points=0, emoji='🏀')
        sport3, _ = Sport.objects.get_or_create(name='Siatkówka', win_points=2, draw_points=1, lose_points=0, emoji='🏐')
        sports = [sport1, sport2, sport3]

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
        
        usernames = ["user1", "user2", "user3", "user4"]
        emails = ["user1@example.com", "user2@example.com", "user3@example.com", "user4@example.com"]
        passwords = ["password1", "password2", "password3", "password4"]

        users_set = []
        for i in range(len(usernames)):
            new_user, _ = User.objects.get_or_create(username=usernames[i], email=emails[i])
            new_user.set_password(passwords[i])  # Ustaw hasło użytkownika
            new_user.save()
            users_set.append(new_user)

        names = ["Alek", "Bartek", "Dawid", "Marek"]
        last_names = ["Widelczyk", "Nozowski", "Szklanecki"]
        positions = ["obronca", "napastnik", "pomocnik"]
        players_set = []
        for i in range(10):
            new_player, _ = Player.objects.get_or_create(first_name=names[i%len(names)], last_name=last_names[i%len(last_names)], position=positions[i % len(positions)], player_number=i)
            players_set.append(new_player)

        departments = [] 
        for i in range(25):
            new_department, _ =  Department.objects.get_or_create(name=f'W{i}')
            departments.append(new_department)
        
        teams = []
        for i in range(25):
            new_team, _ = Team.objects.get_or_create(name=f"Zespol {chr(ord('A')+i)}", department=departments[i], sport=sports[i%len(sports)], capitan=users_set[i%len(users_set)], edition=edition)
            new_team.players.set(players_set)
            teams.append(new_team)
        
        for i in range(8):
            for j in range(i, 8):
                Match.objects.get_or_create(team_one=teams[i], team_two=teams[j], start_time=f'2024-10-{max(10, i+j)} 20:50', end_time=f'2024-10-{max(10, i+j)} 22:50', score_team_one=(i+j)%4, score_team_two=(i+j+1)%3)

        from ligapwr.models import calculate_all_points
        calculate_all_points()

        print ("Dummy data added")

        
