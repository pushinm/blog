from django.db import models



# Create your models here.
class Feedback(models.Model):
    name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Номер', max_length=12)
    email = models.EmailField('email')
    text = models.TextField('Обратная связь')

    def __str__(self) -> str:
        return f'{self.name} - {self.text[:10]}'

    class Meta:
        ordering = ['email', ]