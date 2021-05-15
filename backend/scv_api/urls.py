from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from scv_api.views import TournamentView, TeamView, MatchDayView, MatchView

router = routers.DefaultRouter()
router.register(r'tournament', TournamentView)
router.register(r'team', TeamView)
router.register(r'matchday', MatchDayView)
router.register(r'match', MatchView)

urlpatterns = [
    path('api/', include(router.urls)),
]