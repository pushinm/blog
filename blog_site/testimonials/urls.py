from django.urls import path
from .views import create_testimonial


app_name = 'comment'


urlpatterns = [
    path('', create_testimonial, name='create_comment')
]
