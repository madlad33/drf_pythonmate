# Generated by Django 3.1.5 on 2021-01-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('repeat', models.CharField(choices=[('None', 'None'), ('Daily', 'Daily'), ('Weekly', 'Weekly')], max_length=12)),
                ('select_shift', models.CharField(choices=[('Morning Shift - 5am to 9am ', 'Morning Shift - 5am to 9am ')], max_length=200)),
                ('weekdays', models.CharField(max_length=15)),
            ],
        ),
    ]
