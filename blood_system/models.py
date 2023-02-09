from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Register_as_Donor(models.Model):
    Blood_Type = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    Disease = (
        ('HIV', 'HIV'),
        ('Malaria within this week', 'Malaria within this week'),
        ('None', 'None'),
    )
    
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),

    )

    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(max_length=15, null=True)
    age = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=20, null=True, choices=Gender)
    email = models.CharField(max_length=20, null=True)
    phone= models.CharField(max_length=20, null=True)
    address= models.CharField(max_length=20 ,null=True)
    blood_group = models.CharField(max_length=20 ,null=True, choices=Blood_Type)
    sickness = models.CharField(max_length=50, choices = Disease)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
        


class Request_for_blood(models.Model):
    Blood_Type = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    
    title = models.CharField(max_length=25, null=True)
    blood_unit = models.CharField(max_length=25, null=True)
    patient_name = models.CharField(max_length=25, null=True)
    purpose = models.CharField(max_length=25, null=True)
    blood_group = models.CharField(max_length=20 ,null=True, choices=Blood_Type)
    mobile_number = models.CharField(max_length=25, null=True)
    patient_age = models.CharField(max_length=25, null=True)
    hospital_name = models.CharField(max_length=25, null=True)
    when_need_blood = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=25, null=True)
    details = models.TextField(max_length=50, null=True)
    
    def __str__(self):
       return self.patient_name

class Topic(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(User, related_name = 'participants', blank=True)
    title = models.CharField(max_length=500)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['-date_updated' , '-date_created']


    def __str__(self):
        return self.title



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    room = models.ForeignKey(Room, on_delete = models.CASCADE )
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated' , '-date_created']

    def __str__(self):
        return self.body[0:50]
