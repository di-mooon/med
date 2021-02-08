from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    photo = models.ImageField('Изображение',upload_to='static/')
    name = models.CharField('Фамилия Имя Отчество', max_length=50)
    specialty = models.CharField('Специальность', max_length=50)
    work_experience = models.CharField('Опыт работы', max_length=50)

    def __str__(self):
        return self.name


class Card_comments(models.Model):
    comment = models.TextField('Отзыв', max_length=50)
    data = models.DateField('Дата')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Врач')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.user.username


