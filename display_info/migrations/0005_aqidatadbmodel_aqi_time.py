# Generated by Django 4.2.1 on 2023-05-04 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('display_info', '0004_alter_aqidatadbmodel_station_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aqidatadbmodel',
            name='aqi_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]