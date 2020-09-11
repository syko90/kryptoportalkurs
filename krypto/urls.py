from django.urls import path
from . import views

urlpatterns = [
    path('', views.wydarzenia, name="wydarzenia"),
    path('blog/', views.blog, name='blog'),
    path('ceny/', views.ceny, name='ceny'),
 ]