# Generated by Django 3.1.5 on 2021-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_hospital', '0004_auto_20210111_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='arrival_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='weekdays',
            field=models.BooleanField(default=False),
        ),
    ]
