from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import Shift
import datetime

WEEKDAYS_CHOICES = (
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday')

)

class ShiftSerializer(serializers.ModelSerializer):
    """Serializer for the form model"""
    weekdays_multi = serializers.MultipleChoiceField(choices=WEEKDAYS_CHOICES)
    username = serializers.CharField(source="user.email",read_only=True)
    class Meta:
        model = Shift
        fields = ('username','id', 'start_date', 'arrival_time', 'departure_time', 'repeat', 'select_shift', 'weekdays','weekdays_multi')


    extra_kwargs = {
        'user': {'read_only': True},


    }
