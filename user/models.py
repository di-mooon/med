from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfilePatient(AbstractUser):
    avatar = models.ImageField('Фото', upload_to='static/', default='static/no_foto.jpg', )
    patronymic = models.CharField("Отчество", max_length=50,)
    phone = models.CharField('Телефон', max_length=20,)
    insurance = models.CharField('Страховой полис', max_length=20, blank=True, null=True)
    date = models.DateField('Дата рождения', blank=True, null=True)
    slug = models.SlugField("URL", max_length=50)
    residential_address = models.CharField('Адрес проживания', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = "{}".format(self.username)

    # def get_absolute_url(self):
    #   return reverse('profile', kwargs={'name':self.user.username})


class ProfileDoctor(models.Model):
    photo = models.ImageField('Изображение', upload_to='static/')
    name = models.CharField('Фамилия Имя Отчество', max_length=50)
    specialty = models.CharField('Специальность', max_length=50)
    work_experience = models.CharField('Опыт работы', max_length=50)
    profile = models.OneToOneField(ProfilePatient, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
