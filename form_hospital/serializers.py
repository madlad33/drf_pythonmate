from django.contrib.auth import get_user_model,authenticate
from rest_framework import serializers
from .models import Shift

class ShiftSerializer(serializers.ModelSerializer):
    """Serializer for the form model"""
    class Meta:
        model = Shift
        fields = ('id','start_date','arrival_time','departure_time','repeat','select_shift','weekdays',)

    extra_kwargs = {
        'user': {'read_only': True}

    }


