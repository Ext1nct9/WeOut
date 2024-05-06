from django.urls import path
from .views import EventListView, CreateEventView, EventView

urlpatterns = [
    path('event/', EventListView.as_view()),
    path("create-event/", CreateEventView.as_view()),
    path("event/<uuid:pk>/", EventView.as_view()),

]