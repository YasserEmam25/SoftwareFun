from django.shortcuts import render
from .models import Game
from SoftwareFun import settings
# Create your views here.


def index(request):

    games = Game.objects.all()

    games1 = games[0:3]
    games2 = games[3: 6]
    games3 = games[6:9]

    for game in games3:
        print(game)

    return render(request, "index.html",
                  {'all_games': games, 'media_url': settings.MEDIA_URL})
