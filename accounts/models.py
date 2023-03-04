from django.contrib.auth.models import User
from django.db import models



class PatientsProfile(models.Model):
    id = models.CharField(max_length=18, primary_key=True, editable=False, unique=True)
    patient = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(blank=False)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['name']

    def __str__(self):
        return f'{self.patient}'


class CounsellorsProfile(models.Model):
    id  = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    counsellor = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=14, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    dob = models.DateField(blank=False)

    is_counsellor = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Counsellors'
        ordering = ['counsellor']

    def __str__(self):
        return f'{self.counsellor}'

