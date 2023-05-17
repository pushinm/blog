from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        moel = Blog
        fields = '__all__'
