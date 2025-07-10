from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('matches-per-year/', matches_per_year, name='matches_per_year'),
    path('matches-won-per-team-per-year/', matches_won_per_team_per_year,
         name='matches_won_per_team_per_year'),
    path('extra-runs-2016/', extra_runs_conceded_per_team_in_2016,
         name='extra_runs_conceded_per_team_in_2016'),
    path('top-economical-bowlers-2015/', top_10_economical_bowlers_in_2015,
         name='top_10_economical_bowlers_in_2015'),
    path('matches-per-year-chart/', matches_per_year_chart,
         name='matches_per_year_chart'),
    path('matches-won-per-team-per-year-chart/', matches_won_per_team_per_year_chart,
         name='matches_won_per_team_per_year_chart'),
    path('extra-runs-2016-chart/', extra_runs_conceded_per_team_in_2016_chart,
         name='extra_runs_conceded_per_team_in_2016_chart'),
    path('top-economical-bowlers-2015-chart/', top_10_economical_bowlers_in_2015_chart,
         name='top_10_economical_bowlers_in_2015_chart'),

]
