# Generated by Django 3.1.5 on 2021-01-11 09:52

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('form_hospital', '0006_auto_20210111_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='weekdays',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shift',
            name='weekdays_multi',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=56),
        ),
        migrations.DeleteModel(
            name='Weekdays',
        ),
    ]
