from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import User

from django.views.generic import CreateView, DetailView

from .forms import UserCreatingForm


# Create your views here.


class CreateUser(CreateView):
    model = User
    form_class = UserCreatingForm
    template_name = 'forms_and_reg/user_registration.html'
    success_url = '/'


class UserDetail(DetailView):
    model = User
    template_name = 'pages/author_detail.html'
    context_object_name = 'current_user'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('author_of_blog')

        return queryset