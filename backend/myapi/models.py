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



class Organizer(AbstractUser):
    company = models.CharField(max_length=200, null = True, blank = True)
    bio = HTMLField(null = True, blank = True, default = "Organizer Bio")
    events = models.ManyToManyField(Event, related_name= 'organizers', blank=True)
    groups = models.ManyToManyField(Group, related_name='organizer_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='organizer_user_permissions', blank=True)

    def save(self, *args, **kwargs):
        self.is_active = True
        self.is_staff = True
        super().save(*args, **kwargs)
        manage_event_permission = Permission.objects.get(codename='manage_event')
        view_event_permission = Permission.objects.get(codename='view_event')
        create_event_permission = Permission.objects.get(codename='add_event')
        delete_event_permission = Permission.objects.get(codename='delete_event')
        create_tag_permission = Permission.objects.get(codename='add_tag')
        view_tag_permission = Permission.objects.get(codename='view_tag')
        self.user_permissions.add(manage_event_permission, view_event_permission, create_event_permission, delete_event_permission, create_tag_permission, view_tag_permission)
    
    def __str__(self):
        return self.username
    
