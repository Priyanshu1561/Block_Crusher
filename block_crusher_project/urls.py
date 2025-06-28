from django.contrib import admin
from django.urls import path
from block_crusher.views import game_view  # Import from block_crusher app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_view, name='game'),  # Set the path for the game view
]
