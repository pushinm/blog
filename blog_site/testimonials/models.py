from django.db import models

from blog.models import Blog
from blog.additional_funcs import get_substring_before_separator
from django.db import transaction
# from users_.models import User

# Create your models here.

class Testimonial(models.Model):
    testimonial = models.TextField(verbose_name='Отзыв')
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    active = models.BooleanField(verbose_name='Активен', default=True)
    blog = models.ForeignKey(to=Blog, on_delete=models.DO_NOTHING, verbose_name='Блог', related_name='blog_of_tes')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['create_at',]

    def __str__(self) -> str:
        return f'{get_substring_before_separator(self.testimonial, ".")}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('', kwargs={'pk': self.pk})