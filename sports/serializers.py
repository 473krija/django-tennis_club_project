
from rest_framework import serializers
from .models import *

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class TournamentScheduleSerializer(serializers.HyperlinkedModelSerializer):
    tournament = serializers.SlugRelatedField(queryset = Tournament.objects.all(), slug_field = 'sportsevent')
    venue = serializers.SlugRelatedField(queryset = Venue.objects.all(), slug_field = 'name')

    class Meta:
        model = TournamentSchedule
        fields = '__all__'

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    tournament_schedule = serializers.SlugRelatedField(queryset = TournamentSchedule.objects.all(), slug_field = 'tournament__sportsevent')
    equipment = serializers.SlugRelatedField(queryset = Equipment.objects.all(), slug_field = 'name')

    class Meta:
        model = EquipmentAssignment
        fields = '__all__'
    