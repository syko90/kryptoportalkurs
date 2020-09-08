from django.urls import path
from . import views

urlpatterns = [
    path('', views.wydarzenia, name="wydarzenia")
]