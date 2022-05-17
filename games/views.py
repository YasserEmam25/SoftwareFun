from django.shortcuts import render

# Create your views here.


def index(request):

    games = []

    return render(request, "index.html", {'games': games})
