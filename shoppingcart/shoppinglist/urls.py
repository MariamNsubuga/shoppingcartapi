# app_name/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('register/', UserCreateView.as_view(), name='user-create'),
    # path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', CustomUserRegistrationView.as_view(),
         name='user-registration'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
    path('see/', see, name='see'),
]
