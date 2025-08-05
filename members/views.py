"""
Views for the Members app of the Tennis Club project.
"""

from django.shortcuts import render
from members.models import Member
from sports.models import *

def members(request):
    """Display the list of members."""
    mymembers = Member.objects.all().values()
    context = {'mymembers': mymembers}
    return render(request, 'all_members.html', context)


def details(request, member_id):
    """Display the details of a single member."""
    mymember = Member.objects.get(id=member_id)
    context = {'mymember': mymember}
    return render(request, 'details.html', context)


def main(request):
    """Load the main HTML page."""
    members = Member.objects.all()
    tournaments = Tournament.objects.all()  # ✅ Fetch tournaments
    tournament_schedules = TournamentSchedule.objects.all()
    equipments = Equipment.objects.all()
    equipment_assignments = EquipmentAssignment.objects.all()

    context = {
        'members': members,
        'tournaments': tournaments,
        'tournament_schedules' : tournament_schedules,
        'equipments' : equipments,
        'equipment_assignments' : equipment_assignments,
        
    }
    return render(request, 'main.html')


def testing(request):
    """Display the test page with a list of fruits."""
    context = {'fruits': ['Apple', 'Banana', 'Cherry']}
    return render(request, 'template.html', context)
