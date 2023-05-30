"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


class MyLoginView(LoginView):
    success_url = 'sldmco;sfiondiosvios'
    template_name = 'logs/login.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog.blog')),
    path('users/', include('users_.urls', namespace='users_.users')),
    path('feedback/', include('feedback.urls', namespace='feedback.f')),
    path('comments/', include('testimonials.urls', namespace='testimonials.comment')),
    # path('captcha/', include('captcha.urls')),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logs/logout.html'), name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
