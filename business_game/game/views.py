from django.shortcuts import render
from .models import Game, Player, Property

def index(request):
    return render(request, 'game/index.html')

# Add more views to handle game actions
