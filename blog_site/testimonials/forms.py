from django import forms
from .models import Testimonial


class CommentForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('testimonial', 'blog',)