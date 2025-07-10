from pathlib import Path
import csv
from datetime import datetime
from django.db import transaction
from django.core.management.base import BaseCommand
from ipl_project_app.models import Matches, Deliveries


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        matches_filepath = base_dir/'data'/'matches.csv'
        deliveries_filepath = base_dir/'data'/'deliveries.csv'
        try:
            with transaction.atomic():
                self.import_matches_data(matches_filepath)
                self.import_deliveries_data(deliveries_filepath)

        except Exception as err:
            print('Failed in importing csv files : ', err)

    def import_matches_data(self, path):
        with open(path, 'r') as matches_data:
            data_reader = csv.DictReader(matches_data)
            for match in data_reader:
                Matches.objects.create(
                    id=int(match['id']),
                    season=int(match['season']),
                    city=match['city'] or None,
                    date=datetime.strptime(match['date'], '%Y-%m-%d'),
                    team1=match['team1'],
                    team2=match['team2'],
                    toss_winner=match['toss_winner'],
                    toss_decision=match['toss_decision'],
                    result=match['result'],
                    dl_applied=int(match['dl_applied']),
                    winner=match['winner'] or None,
                    win_by_runs=int(match['win_by_runs']),
                    win_by_wickets=int(match['win_by_wickets']),
                    player_of_match=match['player_of_match'] or None,
                    venue=match['venue'],
                    umpire1=match['umpire1'] or None,
                    umpire2=match['umpire2'] or None,
                    umpire3=match['umpire3'] or None
                )

    def import_deliveries_data(self, path):
        with open(path, 'r') as deliveries_data:
            data_reader = csv.DictReader(deliveries_data)
            for delivery in data_reader:
                Deliveries.objects.create(
                    match_id=Matches.objects.get(id=int(delivery['match_id'])),
                    inning=int(delivery['inning']),
                    batting_team=delivery['batting_team'],
                    bowling_team=delivery['bowling_team'],
                    over=int(delivery['over']),
                    ball=int(delivery['ball']),
                    batsman=delivery['batsman'],
                    non_striker=delivery['non_striker'],
                    bowler=delivery['bowler'],
                    is_super_over=int(delivery['is_super_over']),
                    wide_runs=int(delivery['wide_runs']),
                    bye_runs=int(delivery['bye_runs']),
                    legbye_runs=int(delivery['legbye_runs']),
                    noball_runs=int(delivery['noball_runs']),
                    penalty_runs=int(delivery['penalty_runs']),
                    batsman_runs=int(delivery['batsman_runs']),
                    extra_runs=int(delivery['extra_runs']),
                    total_runs=int(delivery['total_runs']),
                    player_dismissed=delivery['player_dismissed'] or None,
                    dismissal_kind=delivery['dismissal_kind'] or None,
                    fielder=delivery['fielder'] or None
                )
