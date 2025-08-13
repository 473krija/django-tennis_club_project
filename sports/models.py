
from django.db import models

class Tournament(models.Model):
    sportsevent = models.CharField(max_length=255)
    participant = models.ForeignKey('members.Member', on_delete=models.CASCADE)
    date_held = models.DateField(null=True)

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.location})"

class TournamentSchedule(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    schedule_date = models.DateField()

    def __str__(self):
        return f"{self.tournament.sportsevent} at {self.venue.name} on {self.schedule_date}"
    
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length=50, choices=[
        ('New', 'New'),
        ('Used', 'Used'),
        ('Damaged', 'Damaged')
    ])

    def __str__(self):
        return f"{self.name} ({self.quantity} - {self.condition})"

class EquipmentAssignment(models.Model):
    tournament_schedule = models.ForeignKey(TournamentSchedule, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.assigned_quantity} {self.equipment.name} for {self.tournament_schedule}"


     