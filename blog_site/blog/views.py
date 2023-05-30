from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, UpdateView
from testimonials.models import Testimonial

from testimonials.models import Testimonial
from .models import Blog
from .forms import BlogForm
from django.forms import modelformset_factory
from testimonials.forms import CommentForm
from users_.models import User
# from icecream import ic
from django.db import transaction


# Create your views here.

class AllPAges(ListView):
    model = Blog
    template_name = 'pages/all_pages.html'
    context_object_name = 'blogs'
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['authors'] = User.objects.all()
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
    if request.method == 'GET':
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
        #return render(request=request, template_name=template_name, context={'text': text})
    return render(request=request, template_name=template_name, context={'text': '1'})