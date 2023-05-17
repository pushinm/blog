from django.urls import path
from .views import create_feedback


app_name = 'f'


urlpatterns = [
    path('', create_feedback, name='feedback')
]
