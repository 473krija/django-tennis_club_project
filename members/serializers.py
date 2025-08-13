
from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    member = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field = 'firstname')

    class Meta:
        model = Membership
        fields = '__all__'

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    player1 = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field='firstname')
    player2 = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field='firstname')
    winner = serializers.SlugRelatedField(queryset=Member.objects.all(), slug_field='firstname', allow_null=True)
    coach = serializers.SlugRelatedField(queryset=Coach.objects.all(), slug_field='name', allow_null=True)

    class Meta:
        model = Match
        fields = ['url', 'player1', 'player2', 'match_date', 'winner', 'coach']
