from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse
from .models import Feedback
from .forms import FeedbackForm
# from icecream import ic
from django.shortcuts import render
from django.core.signing import Signer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy


# Create your views here.


# @method_decorator(login_required, name='dispatch')
# class FeedbackListView(ListView):
#     model = Feedback
#     template_name = 'pages/all_testims.html'
#     context_object_name = 'feedbacks'


# @method_decorator(login_required, name='dispatch')
# @method_decorator(PermissionRequiredMixin, name='dispatch')
# class FeedbackCreateView(CreateView):
#     model = Feedback
#     fields = '__all__'
#     success_url = '/'



# @method_decorator(login_required, name='dispatch')
# @method_decorator(PermissionRequiredMixin(name='feedback.change_feedback'), name='dispatch')
# class FeedbackUpdateView(UpdateView):
#     model = Feedback
#     fields = '__all__'
#     success_url = '/'
#
#
# @method_decorator(login_required, name=dispatch)
# @method_decorator(PermissionRequiredMixin(name='feedback.delete_feedback'), name='dispatch')
# class FeedbackDeleteView(DeleteView):
#     model = Feedback
#     success_url = '/'

def create_feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        name = form.cleaned_data.get("name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        f_data = f'{name}_{phone}_{email}'
        signer = Signer()
        signed_data = signer.sign(f_data)
        print(signed_data)
        responce = redirect(reverse('blog:all_pages'))
        return responce
    return render(request=request, template_name='forms_and_reg/form_feedback.html', context={'form': form})