from django.urls import path
from . import views

urlpatterns = [
    path("", views.CoachListView.as_view(), name="coach_list"),
    path("<int:pk>/", views.CoachDetailView.as_view(), name="coach_detail"),
]
