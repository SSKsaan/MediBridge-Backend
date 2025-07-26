from django.db import models
from django.conf import settings

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=99)
    contact = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])

    def __str__(self):
        return f"{self.name} ({self.contact})"

class Appointment(models.Model):
    # User Request:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    speciality = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    area = models.CharField(max_length=100)
    preferred_gender = models.CharField(max_length=10, choices=[
        ('any', 'Any'),
        ('male', 'Male'),
        ('female', 'Female')
    ], default='any')
    budget = models.CharField(max_length=10, choices=[
        ('any', 'Any'),
        ('low', '$'),
        ('medium', '$$'),
        ('high', '$$$')
    ], default='any')

    note = models.TextField(null=True, blank=True)

    # Status:
    status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('waiting', 'Waiting'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    # Appointment Response:
    hospital = models.CharField(max_length=200, null=True, blank=True)
    doctor = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    fees = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"[{self.status}] {self.user.username} - {self.speciality}"
