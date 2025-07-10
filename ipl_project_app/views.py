from django.shortcuts import render
from .models import Matches, Deliveries
from django.db.models import Count, Sum, Case, When
from django.db.models.functions import Round

from django.http import JsonResponse
# Create your views here.

# -------------------------------- Json outputs --------------------------------


def index(request):
    return render(request, "index.html")

def matches_per_year(request):
    result_data = Matches.objects.values('season').annotate(
        matches_count=Count('id')).order_by('season')
    result_data = JsonResponse(list(result_data), safe=False)
    return result_data


def matches_won_per_team_per_year(request):
    result_data = Matches.objects.values('season', 'winner').annotate(
        wins=Count('id')).exclude(winner__isnull=True).order_by('season', 'wins')
    result_data = JsonResponse(list(result_data), safe=False)
    return result_data


def extra_runs_conceded_per_team_in_2016(request):
    result_data = Deliveries.objects.filter(match_id__season=2016).values(
        'bowling_team').annotate(extra_runs=Sum('extra_runs')).order_by('extra_runs')
    result_data = JsonResponse(list(result_data), safe=False)
    return result_data


def top_10_economical_bowlers_in_2015(request):
    result_data = Deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(economy=Round(((Sum('wide_runs') + Sum('batsman_runs') + Sum('noball_runs'))*6.0/(Sum(
        Case(
            When(wide_runs=0, noball_runs=0, then=1),
            default=0
        )
    ))), 2)).order_by('economy')[:10]
    result_data = JsonResponse(list(result_data), safe=False)
    return result_data

# --------------------------------------- Charts ---------------------------------------


def matches_per_year_chart(request):
    return render(request, "matches_per_year.html")


def matches_won_per_team_per_year_chart(request):
    return render(request, "matches_won_per_team_per_year.html")


def extra_runs_conceded_per_team_in_2016_chart(request):
    return render(request, "extra_runs_conceded_per_team_in_2016.html")


def top_10_economical_bowlers_in_2015_chart(request):
    return render(request, "top_10_economical_bowlers_in_2015.html")
