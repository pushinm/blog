from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from testimonials.models import Testimonial
from django.contrib import messages
from testimonials.models import Testimonial
from .models import Blog
from .forms import BlogCreationForm
from django.forms import modelformset_factory
from testimonials.forms import CommentForm
from author.models import Author
from icecream import ic
from django.db import transaction
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# Create your views here.

class CreateBlog(CreateView, SuccessMessageMixin):
    model = Blog
    form_class = BlogCreationForm
    template_name = 'pages/blog_create.html'
    success_url = '/'
    success_message = f'Создана новая статья'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        if self.success_message:
            messages.success(self.request, self.success_message)
        form.save()
        return super().form_valid(form)


class AllPAges(ListView, HttpResponse):
    model = Blog
    template_name = 'pages/all_pages.html'
    context_object_name = 'blogs'
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['authors'] = Author.objects.all()
        return context


class BlogDetail(DetailView):
    model = Blog
    template_name = 'pages/page_detail.html'
    context_object_name = 'blog'


def blog_update(request):
    BlogFormSet = modelformset_factory(Blog, fields='__all__')
    if request.method == 'POST':
        formset = BlogFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Статья исправлена')
            return redirect('/')
    else:
        formset = BlogFormSet()
    context = {
        'formset': formset
    }
    return render(request=request, template_name='pages/page_edit.html', context=context)


def delete_article(request, pk):
    article = get_object_or_404(Blog, pk=pk)
    print(article)
    if request.method == 'GET' and request.user == article.author:
        return article.delete()


def delete_comments(request, pk):
    article = get_object_or_404(Blog, pk=pk)
    comments = article.blog_of_tes.all()
    print(comments)
    if request.method == 'GET':
        return comments.delete()
    # ic(article)
    # ic(comments)


@transaction.atomic
def delete_blog_with_comments(request, pk):
    delete_comments(request, pk)
    delete_article(request, pk)
    return redirect('/')


def add_comment(request, pk):
    template_name = 'pages/page_detail.html'
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        text = request.POST.get('message')
        print(text)
        Testimonial.objects.create(testimonial=text, blog=blog)
        return redirect(f'/blogdetail-{blog.pk}/')
        # return render(request=request, template_name=template_name, context={'text': text})
    return render(request=request, template_name=template_name, context={'text': '1'})
