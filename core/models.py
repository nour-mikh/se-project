from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    mobile_number = models.CharField(max_length=50, blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)


class InterviewCategory(models.Model):
    name = models.CharField(max_length=50)


class Interview(models.Model):
    interviewer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_time = models.DateTimeField()
    category = models.ForeignKey(InterviewCategory, null=True, on_delete=models.SET_NULL)
    duration = models.DurationField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('Cash', 'Cash'),
        ('Online', 'Online'),
    )
    payment = models.CharField(max_length=200, choices=PAYMENT_CHOICES)


class Booking(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.SET_NULL, blank=True, null=True)
    interviewer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    payment =  models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)


class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    
