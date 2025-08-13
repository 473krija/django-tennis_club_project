from django.urls import path
from . import views

urlpatterns = [
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('schedules/', views.tournament_schedule_list, name='tournament_schedule_list'),
    path('equipments/', views.equipment_list, name='equipment_list'),
    path('equipment-assignments/', views.equipment_assignment_list, name='equipment_assignment_list'),
]
