from django.urls import path
from .views import registerUser, home

urlpatterns = [
    path('register/', registerUser, name='register'),
    path('', home, name='home'),
]
