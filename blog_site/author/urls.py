from django.urls import path
from .views import AuthorDetail, CreateAuthor

app_name = 'authors'

urlpatterns = [
    path('create_author/', CreateAuthor.as_view(), name='create_author'),
    path('current/<int:pk>/', AuthorDetail.as_view(), name='author_detail')
]
