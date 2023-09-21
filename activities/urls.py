from django.urls import path
from .views import Activities

urlpatterns = [
    path("", Activities.as_view()),
]
