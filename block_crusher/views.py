from django.shortcuts import render

def game_view(request):
    return render(request, 'block_crusher/game.html')
