from django.urls import path
from .views import AllPAges, BlogDetail, blog_update

app_name = 'blog'


urlpatterns = [
    path('', AllPAges.as_view(), name='all_pages'),
    path('blogdetail-<int:pk>/', BlogDetail.as_view(), name='detail_page'),
    path('update_all/', blog_update, name='update_all'),
]