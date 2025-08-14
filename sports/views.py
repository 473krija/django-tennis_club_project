from django.shortcuts import render
from .models import Tournament
from .models import TournamentSchedule
from .models import EquipmentAssignment, Equipment
from rest_framework import viewsets
from .serializers import *

def tournament_list(request):
    tournaments= Tournament.objects.all()
    return render(request, 'tournament_list.html',{'tournaments': tournaments})

def tournament_schedule_list(request):
    schedules = TournamentSchedule.objects.select_related('tournament', 'venue').all()
    return render(request, 'tournament_schedule_list.html', {'schedules': schedules})

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html',{'equipments' : equipments})

def equipment_assignment_list(request):
    #import pdb;pdb.set_trace();
    assignments = EquipmentAssignment.objects.all()
    return render(request, 'equipment_assignment_list.html', {'assignments' : assignments})

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class TournamentScheduleViewSet(viewsets.ModelViewSet):
    queryset = TournamentSchedule.objects.all()
    serializer_class = TournamentScheduleSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class EquipmentAssignmentViewSet(viewsets.ModelViewSet):
    queryset = EquipmentAssignment.objects.all()
    serializer_class = EquipmentAssignmentSerializer


