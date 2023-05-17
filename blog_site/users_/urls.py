from django.urls import path
from .views import CreateUser, UserDetail

app_name = 'users'

urlpatterns = [
    path('create_user/', CreateUser.as_view(), name='create_user'),
    path('current/<int:pk>/', UserDetail.as_view(), name='author_detail')
]
