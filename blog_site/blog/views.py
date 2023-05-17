from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, FormView, UpdateView

from testimonials.models import Testimonial
from .models import Blog
from .forms import BlogForm
from django.forms import modelformset_factory
from testimonials.forms import CommentForm
from users_.models import User


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
