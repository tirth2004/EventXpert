from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class TestModel(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')

class Category(models.Model):
    category_name= models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class OrganisationEvent(models.Model):
    event_name=models.CharField(max_length=100, help_text='Enter the Event Name')
    event_date=models.DateField()
    venue = models.CharField(max_length=150, help_text='Enter Venue')
    description = models.TextField(help_text='Enter Description of Event')
    category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True,help_text='Select category for this event')
    registered_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.event_name
    
  
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def register_for_event(self,event):
        event.registered_students += 1  # Increment the count of registered students for the event
        event.save()

class EventRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # You can use your Student model here
    event = models.ForeignKey(OrganisationEvent, on_delete=models.CASCADE)  # Replace 'Event' with your event model


