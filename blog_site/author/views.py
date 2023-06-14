from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .models import Author
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from .forms import UserCreatingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate, logout
from .forms import AuthAuthorForm
from django.http.response import HttpResponseBase, HttpResponseForbidden
from django.contrib import messages


# Create your views here.


class AuthorLogin(LoginView):
    template_name = 'logs/login.html'
    form_class = AuthAuthorForm
    success_url = reverse_lazy('blog:blog')

    def dispatch(self, request, *args, **kwargs):
        if 'user' in request.COOKIES:
            username = request.COOKIES['user']
            password = request.COOKIES['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                responce = HttpResponseForbidden("Вы уже сделали вход так как мы использовали куки. до этого вы регистрировались. вот мы и запомнили эти данные но ради безопасности сразу же удалили эти куки")
                responce.delete_cookie('user')
                responce.delete_cookie('password')
                return responce
        return super().dispatch(request, *args, **kwargs)


class CreateAuthor(CreateView):
    form_class = UserCreatingForm
    template_name = 'forms_and_reg/user_registration.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = UserCreatingForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            logout(request)

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login(request, new_user)
            responce = redirect('/')
            responce.set_cookie('user', f'{username}')
            responce.set_cookie('password', f'{password}')
            return responce
        else:
            return render(request, self.template_name, {'form': form})


class AuthorDetail(DetailView):
    model = Author
    template_name = 'pages/author_detail.html'
    context_object_name = 'current_author'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('author_of_blog')

        return queryset
