from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from scv_api.models import Tournament, Team, MatchDay, Match
from scv_api.serializers import TournamentSerializer, TeamSerializer, MatchDaySerializer, MatchSerializer


class TournamentView(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MatchDayView(viewsets.ModelViewSet):
    queryset = MatchDay.objects.all()
    serializer_class = MatchDaySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('tournament',)


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('matchday',)
