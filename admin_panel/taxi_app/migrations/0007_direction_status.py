# Generated by Django 5.1.3 on 2024-12-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_app', '0006_remove_direction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='status',
            field=models.SmallIntegerField(default=1),
        ),
    ]
