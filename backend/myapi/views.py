from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status, filters
from rest_framework.views import APIView
from .models import Event
from .serializers import CreateEventSerializer, EventSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Organizer


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location', 'tags__name']


class CreateEventView(APIView):
    serializer_class = CreateEventSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.title
            description = serializer.data.description
            date = serializer.data.date
            time = serializer.data.time
            location = serializer.data.location
            visibility = serializer.data.visibility
            manager = request.user
            event = Event(title=title, description=description, date=date, time=time, location=location, visibility=visibility, manager=manager)
            event.save()
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response({"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST)

class EventView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        event = get_object_or_404(Event, pk=id)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    serializer_class = EventSerializer
    def put(self, request, *args, **kwargs):
        id = kwargs['pk']
        event = get_object_or_404(Event, pk=id)
        serializer = CreateEventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        event = get_object_or_404(Event, pk=id)
        event.delete()
        return Response({"Message": "Event with id `{}` has been deleted.".format(id)}, status=204)    




class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if isinstance(user, Organizer):
                return redirect('organizer_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            # Invalid login
            ...
    else:
        # Display the login form
        ...
