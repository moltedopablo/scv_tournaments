from rest_framework import serializers

from scv_api.models import Tournament, Team, MatchDay, Match


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'teams', 'quantity', 'positions']

    def validate_quantity(self, value):
        if value % 2 != 0:
            raise serializers.ValidationError('Must be even')

        if value < 2:
            raise serializers.ValidationError('Must be at least 2')

        if value > Team.objects.count():
            raise serializers.ValidationError('Must be inferior to the number of teams available')

        return value


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
        depth = 1
