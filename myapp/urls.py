from django.urls import path
from . import views


urlpatterns = [
    path('page5/', views.page5, name='page5'),
    ]