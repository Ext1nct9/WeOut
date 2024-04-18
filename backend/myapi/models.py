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
    manager = models.ForeignKey('Organizer', on_delete=models.CASCADE,  related_name='managed_events')
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
    events = models.ManyToManyField(Event, related_name= 'tags', blank=True)

    def __str__(self):
        return self.name

class Organizer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(null = True, blank = True, default = "Organizer Bio")
    events = models.ManyToManyField(Event, related_name= 'organizers', blank=True)
    groups = models.ManyToManyField(Group, related_name='organizer_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='organizer_user_permissions', blank=True)


    def __str__(self):
        return self.username

