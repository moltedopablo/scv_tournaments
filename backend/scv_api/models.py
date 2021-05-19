import itertools
from django.db import models
from django.db.models import F


class Team(models.Model):
    name = models.CharField(max_length=128)


class Tournament(models.Model):
    name = models.CharField(max_length=128)
    teams = models.ManyToManyField(Team, through='TournamentTeam')
    quantity = models.IntegerField()

    @property
    def positions(self):
        teams = TournamentTeam.objects.filter(tournament=self)
        positions = []
        for tt in teams:
            positions.append({
                'name': tt.team.name,
                'won': tt.matches_won,
                'lost': tt.matches_lost,
                'tie': tt.matches_tie,
                'score': tt.matches_won * 3 + tt.matches_tie})
        return sorted(positions, key=lambda i: i['score'], reverse=True)

    def add_teams(self, teams):
        for team in teams:
            tt = TournamentTeam(tournament=self, team=team)
            tt.save()

    def generate_matches(self):
        teams = list(TournamentTeam.objects.filter(tournament=self).values_list('team_id', flat=True))
        n = len(teams)
        matches = []
        matchdays = []
        for fixture in range(1, n):
            for i in range(n // 2):
                matches.append((teams[i], teams[n - 1 - i]))
            teams.insert(1, teams.pop())
            matchdays.insert(len(matchdays) // 2, matches)
            matches = []

        i = 0
        for matchday in matchdays:
            md = MatchDay(tournament=self, number=i + 1)
            md.save()
            i += 1
            for match in matchday:
                home_team = Team.objects.get(pk=match[0])
                away_team = Team.objects.get(pk=match[1])
                m = Match(matchday=md, home_team=home_team, away_team=away_team)
                m.save()

    def save(self, *args, **kwargs):
        super(Tournament, self).save(*args, **kwargs)
        teams = Team.objects.all().order_by('?')[:self.quantity]
        self.add_teams(teams)
        self.generate_matches()


class TournamentTeam(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    @property
    def matches_won(self):
        home_won = Match.objects.filter(matchday__tournament=self.tournament, home_team=self.team,
                                        home_goals__gt=F('away_goals')).count()
        away_won = Match.objects.filter(matchday__tournament=self.tournament, away_team=self.team,
                                        away_goals__gt=F('home_goals')).count()
        return home_won + away_won

    @property
    def matches_lost(self):
        home_lost = Match.objects.filter(matchday__tournament=self.tournament, home_team=self.team,
                                         home_goals__lt=F('away_goals')).count()
        away_lost = Match.objects.filter(matchday__tournament=self.tournament, away_team=self.team,
                                         away_goals__lt=F('home_goals')).count()
        return home_lost + away_lost

    @property
    def matches_won(self):
        home_won = Match.objects.filter(matchday__tournament=self.tournament, home_team=self.team,
                                        home_goals__gt=F('away_goals')).count()
        away_won = Match.objects.filter(matchday__tournament=self.tournament, away_team=self.team,
                                        away_goals__gt=F('home_goals')).count()
        return home_won + away_won

    @property
    def matches_tie(self):
        home_tie = Match.objects.filter(matchday__tournament=self.tournament, home_team=self.team,
                                        home_goals=F('away_goals')).count()
        away_tie = Match.objects.filter(matchday__tournament=self.tournament, away_team=self.team,
                                        away_goals=F('home_goals')).count()
        return home_tie + away_tie


class MatchDay(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    number = models.IntegerField()


class Match(models.Model):
    matchday = models.ForeignKey(MatchDay, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='match_away_team')
    home_goals = models.IntegerField(null=True, blank=True)
    away_goals = models.IntegerField(null=True, blank=True)
