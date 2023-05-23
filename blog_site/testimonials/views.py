from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Testimonial
from blog.models import Blog
# Create your views here.

def create_testimonial(request, blog_pk):
    if request.method == 'POST':
        text = request.POST.get('message')
        Testimonial.objects.create(testimonial=text, blog=blog_pk)
        return redirect('/')