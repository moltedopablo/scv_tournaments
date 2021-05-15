import itertools

from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)


class Tournament(models.Model):
    name = models.CharField(max_length=128)
    teams = models.ManyToManyField(Team, through='TournamentTeam')
    quantity = models.IntegerField()

    def add_teams(self, teams):
        for team in teams:
            TournamentTeam = apps.get_model(app_label='scv_api', model_name='TournamentTeam')
            tt = TournamentTeam(tournament=self, team=team)
            tt.save()

    def generate_matches(self):
        TournamentTeam = apps.get_model(app_label='scv_api', model_name='TournamentTeam')
        MatchDay = apps.get_model(app_label='scv_api', model_name='MatchDay')
        Match = apps.get_model(app_label='scv_api', model_name='Match')
        tournament_teams = TournamentTeam.objects.filter(tournament=self).values_list('team_id', flat=True)
        combinations = itertools.combinations(tournament_teams, 2)
        i = 0
        for c in combinations:
            if i % (self.quantity/2) == 0:
                md = MatchDay(tournament=self, number=i + 1)
                md.save()
            home_team = Team.objects.get(pk=c[0])
            away_team = Team.objects.get(pk=c[1])
            m = Match(matchday=md, home_team=home_team, away_team=away_team)
            m.save()
            i += 1

    def save(self, *args, **kwargs):
        super(Tournament, self).save(*args, **kwargs)
        teams = Team.objects.all().order_by('?')[:self.quantity]
        self.add_teams(teams)
        self.generate_matches()


class TournamentTeam(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class MatchDay(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    number = models.IntegerField()


class Match(models.Model):
    matchday = models.ForeignKey(MatchDay, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_away_team')
    home_goals = models.IntegerField(null=True, blank=True)
    away_goals = models.IntegerField(null=True, blank=True)
