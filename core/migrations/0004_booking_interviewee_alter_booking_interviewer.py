# Generated by Django 4.2.6 on 2024-05-06 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_remove_interview_date_time_interview_interview_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='interviewee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interviewee_bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='interviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interviewer_bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
