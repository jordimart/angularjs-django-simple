from rest_framework import viewsets
from app.games.models import Game
from app.api.v1.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer