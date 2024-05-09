from django.db import models
import uuid
import urllib.parse
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null = False, default = "Event Title")
    manager = models.CharField(max_length=200, null = False, default = "Event Manager")
    description = HTMLField(null = True, blank = True, default = "Event Description")
    date = models.DateField(null = False)
    time = models.TimeField(null = True, blank = True)
    location = models.CharField(max_length=200)
    visibility = models.BooleanField(null = False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_location_url(self):
        base_url = "https://www.google.com/maps/search/?api=1"
        query = "&query=" + urllib.parse.quote(self.location)
        return base_url + query

    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null = False, default = "Tag Name")
    events = models.ManyToManyField(Event, related_name= 'tags', blank=True, null = True)

    def __str__(self):
        return self.name



class User(AbstractUser):
    company = models.CharField(max_length=200, null = True, blank = True)
    bio = HTMLField(null = True, blank = True, default = "Organizer Bio")
    events = models.ManyToManyField(Event, related_name= 'Organizers', blank=True)
    groups = models.ManyToManyField(Group, related_name='organizer_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='Organizer_user_permissions', blank=True)
    managed_events = models.ManyToManyField(Event, related_name='managed_events', blank=True)

    def save(self, *args, **kwargs):
        self.is_active = True
        self.is_staff = True
        Group.objects.get(name='Organizers').add(self)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=200, null = False, default = "Group Name")
    permissions = models.ManyToManyField(Permission, related_name='permissions', blank=True)
    members = models.ManyToManyField(User, related_name='members', blank=True)

    def __str__(self):
        return self.name