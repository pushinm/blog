from django.db import models
from author.models import Author
from precise_bbcode.fields import BBCodeTextField
from precise_bbcode.bbcode import get_parser


def generate_docs_upload_path(instance, filename):
    author = instance.author
    return f'files/docs/{author.pk}/{filename}'


# Create your models here.
class Blog(models.Model):
    title = models.CharField('Название блога', max_length=100)
    photo = models.ImageField()
    text = BBCodeTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(verbose_name='', null=True, blank=True)
    author = models.ForeignKey(to=Author, on_delete=models.DO_NOTHING, related_name='author_of_blog')
    additional_docs = models.FileField(upload_to=generate_docs_upload_path, blank=True, null=True)

    def __str__(self):
        return f'{self.title}-{self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
