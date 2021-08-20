from django.db import models
from django.contrib.auth.models import User
from user.models import Profile


class Card(models.Model):
    photo = models.ImageField('Изображение', upload_to='static/')
    name = models.CharField('Фамилия Имя Отчество', max_length=50)
    specialty = models.CharField('Специальность', max_length=50)
    work_experience = models.CharField('Опыт работы', max_length=50)

    def __str__(self):
        return self.name



