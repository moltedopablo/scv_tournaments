from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=128)


class Tournament(models.Model):
    name = models.CharField(max_length=128)
    teams = models.ManyToManyField(Team, through='TournamentTeam')
    quantity = models.IntegerField()


class TournamentTeam(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_as_home = models.BooleanField(default=False)


class MatchDay(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    number = models.IntegerField()


class Match(models.Model):
    matchday = models.ForeignKey(MatchDay, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_away_team')
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
