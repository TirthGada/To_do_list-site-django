# Generated by Django 4.1.7 on 2023-06-29 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
