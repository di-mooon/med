
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from djangoProject1 import settings
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='Пользователь', on_delete=models.CASCADE)
    avatar = models.ImageField('Фото', upload_to='static/', default='static/no_foto.jpg')
    first_name = models.CharField('Имя',max_length=30,blank=True)
    last_name = models.CharField('Фамилия',max_length=50, blank=True)
    patronymic = models.CharField("Отчество", max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    insurance = models.CharField('Страховой полис', max_length=20, blank=True)
    email_two = models.EmailField()
    data = models.DateField('Дата рождения',default='2010-10-10')
    slug=models.SlugField("URL",max_length=50)



    def __str__(self):
        return self.user.username

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        self.slug="{}".format(self.user.username)

    #def get_absolute_url(self):
     #   return reverse('profile', kwargs={'name':self.user.username})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
