from django.db import models
from users_.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField('Название блога', max_length=100)
    photo = models.ImageField()
    text = models.TextField('текст')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(verbose_name='', null=True, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='author_of_blog')
    order = models.SmallIntegerField(db_index=True, default=0)

    def __str__(self):
        return f'{self.title}-{self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['order',]