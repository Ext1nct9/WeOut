from django.urls import path
from .views import EventListView, CreateEventView, EventView, CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('event/', EventListView.as_view()),
    path("create-event/", CreateEventView.as_view()),
    path("event/<uuid:pk>/", EventView.as_view()),
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]