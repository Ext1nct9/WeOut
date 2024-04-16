from rest_framework import serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','name']

class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        event = Event.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            event.tags.add(tag)
        return event

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance.tags.set([])
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        instance.save()
        return instance
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user