from django.shortcuts import render
from .models import Tournament
from .models import TournamentSchedule
from .models import EquipmentAssignment, Equipment

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


