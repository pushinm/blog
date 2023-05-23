from django.urls import path
from .views import AllPAges, BlogDetail, blog_update, delete_blog_with_comments, add_comment
app_name = 'blog'


urlpatterns = [
    path('', AllPAges.as_view(), name='all_pages'),
    path('blogdetail-<int:pk>/', BlogDetail.as_view(), name='detail_page'),
    path('blog/delete/<int:pk>/', delete_blog_with_comments, name='delete_blog'),
    path('blog_add_comment/<int:pk>/', add_comment, name='add_comment'),
    path('update_all/', blog_update, name='update_all'),
]