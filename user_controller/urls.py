from django.urls import path
from .views import ListCreateNormalUser, ListCreateAdmin, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list_and_create_normalusers/', ListCreateNormalUser.as_view()),
    path('list_and_create_admins/', ListCreateAdmin.as_view()),
]