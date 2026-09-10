from django.urls import path
from . import views

urlpatterns = [
    path("", views.PlayerListView.as_view(), name="player_list"),
    path("<int:pk>/", views.PlayerDetailView.as_view(), name="player_detail"),
]
