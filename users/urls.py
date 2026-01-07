from django.urls import path
from .views import student_sign_up, student_login

app_name = 'users'

urlpatterns = [
    path('register/', student_sign_up, name='sign_up'),
    path('login/', student_login, name='login'),
    # path('logout/', views.logout_view, name='logout'),
]