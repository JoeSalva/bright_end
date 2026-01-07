from django.urls import path
from .views import landingpage, control, student

app_name = 'exam'

urlpatterns = [
    path('home/', landingpage, name='landing'),
    path('control/', control, name='admin'),
    path('student/', student, name='student'),
]