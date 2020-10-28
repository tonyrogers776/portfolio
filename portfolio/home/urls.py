from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('music', views.music),
    path('contact', views.contact),
    path('portfolio', views.portfolio)
]