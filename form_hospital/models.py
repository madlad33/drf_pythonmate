from django.db import models
from django.conf import settings
import datetime
# Create your models here.
REPEAT_CHOICES = (
    ('None','None'),
    ('Daily','Daily'),
    ('Weekly','Weekly')
)
SHIFT_CHOICES = (
    ('Morning Shift - 5am to 9am ','Morning Shift - 5am to 9am '),
)


class Shift(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    start_date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    repeat = models.CharField(max_length=12,choices=REPEAT_CHOICES)
    select_shift = models.CharField(max_length=200,choices=SHIFT_CHOICES)
    weekdays = models.BooleanField(default=False)

    def __str__(self):
        return f"Shift {self.id}"

