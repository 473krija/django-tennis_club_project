""" Models for the project"""

from django.db import models


class Member(models.Model):
    """Inserting the required objects into class"""

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Coach(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name

class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)  # FK to Member
    membership_type = models.CharField(max_length=50, choices=[
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Yearly', 'Yearly'),
    ])
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.member} - {self.membership_type}"

class Match(models.Model):
    player1 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='player2_matches')
    match_date = models.DateField()
    winner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='won_matches')
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True)  # Optional

    def __str__(self):
        return f"Match: {self.player1} vs {self.player2} on {self.match_date}"