from django.forms import ModelForm, FileField
from .models import Blog
from django.core.exceptions import ValidationError
from django.core import validators


class BlogCreationForm(ModelForm):
    error_css_class = 'error_class'

    additional_docs = FileField(
        label='Сороводительный документ',
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=(
                    'xlsx',
                    'pdf'
                )
            )
        ],
        error_messages={'invalid_extention': 'Этот формат не поддерживается'}
    )

    class Meta:
        model = Blog
        fields = ['title', 'photo', 'text']
        labels = {
            'title': 'Название блога',
            'photo': 'Фото',
            'text': 'Текст',
            'additional_docs': 'Дополнительные документы'
        }
