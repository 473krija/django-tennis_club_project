from django.contrib import admin
from .models import Tournament
from .models import Venue
from .models import TournamentSchedule, Equipment, EquipmentAssignment

class TournamentAdmin(admin.ModelAdmin):

    list_display = (
        "sportsevent",
        "participant",
        "date_held",
    )

class VenueAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "capacity",
    )

class TournamentScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "tournament",
        "venue",
        "schedule_date",
    )

class EquipmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "quantity",
        "condition",
    )

class EquipmentAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "tournament_schedule",
        "equipment",
        "assigned_quantity",
    )

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(TournamentSchedule, TournamentScheduleAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentAssignment, EquipmentAssignmentAdmin)
