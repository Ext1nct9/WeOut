from django.db import models
import uuid
import urllib.parse
from tinymce.models import HTMLField




# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null = False, default = "Event Title")
    manager = models.CharField(max_length=200, null = False, default = "Event Manager")
    #manager = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
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

