from django.urls import path
from . import views

urlpatterns = [
    path('', views.page5, name='home'),   # homepage
]
