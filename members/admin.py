"""Admin file for the project"""

from django.contrib import admin
from .models import Member, Coach, Membership, Match

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    """Displaying the details as list"""

    list_display = (
        "firstname",
        "lastname",
        "joined_date",
        
    )
class CoachAdmin(admin.ModelAdmin):
    """Displaying the details of Coach model as  list"""

    list_display = (
        "name",
        "experience_years",
    )   

class MembershipAdmin(admin.ModelAdmin):
    """Displaying the details of Membership model as list"""

    list_display = (
        "member",
        "membership_type",
        "start_date",
        "end_date",
    ) 

class MatchAdmin(admin.ModelAdmin):
    """Displaying the details of match model as list"""

    list_display = (
        "player1",
        "player2",
        "match_date",
        "winner",
        "coach",
    )
    list_display_links = (
        "player1",
        "player2",
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Match, MatchAdmin)
