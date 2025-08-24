from django.urls import path
from .views import ListCreateNormalUser, ListCreateAdmin

urlpatterns = [
    path('list_and_create_normalusers/', ListCreateNormalUser.as_view()),
    path('list_and_create_admins/', ListCreateAdmin.as_view()),
]