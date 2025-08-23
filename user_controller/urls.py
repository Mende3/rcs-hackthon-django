from django.urls import path
from .views import listAndCreateUser

urlpatterns = [
    path('list_and_create_users/', listAndCreateUser.as_view()),
]