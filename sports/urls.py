from django.urls import path, include
from . import views
from rest_framework.routers import  DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'tournamentschedules', TournamentScheduleViewSet)
router.register(r'equipments', EquipmentViewSet)
router.register(r'equipmentassignments', EquipmentAssignmentViewSet)

urlpatterns = [
    # path('tournaments/', views.tournament_list, name='tournament_list'),
    # path('schedules/', views.tournament_schedule_list, name='tournament_schedule_list'),
    # path('equipments/', views.equipment_list, name='equipment_list'),
    # path('equipment-assignments/', views.equipment_assignment_list, name='equipment_assignment_list'),
    path('api/', include(router.urls)),
]
