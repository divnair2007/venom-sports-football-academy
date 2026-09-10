from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrainingListView.as_view(), name="training_list"),
]
