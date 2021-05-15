from rest_framework import serializers

from scv_api.models import Tournament, Team, MatchDay, Match


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'teams', 'quantity']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = ['id', 'number', 'tournament']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'matchday', 'home_team', 'away_team', 'home_goals', 'away_goals']
