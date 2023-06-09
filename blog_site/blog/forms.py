from django.forms import ModelForm
from .models import Blog


class BlogCreationForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'photo', 'text', 'additional_docs']
        labels = {
            'title': 'Название блога',
            'photo': 'Фото',
            'text': 'Текст',
            'additional_docs': 'Дополнительные документы'
        }