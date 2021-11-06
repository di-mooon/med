from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone


class UserModelFieldsMixin(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
    )
    patronymic = models.CharField(
        verbose_name="Отчество",
        blank=True, null=True,
        max_length=100,
    )

    class Meta:
        abstract = True


class Profile(AbstractUser):
    is_doctor = models.BooleanField(
        verbose_name='Врач',
        default=False,
    )
    is_patient = models.BooleanField(
        verbose_name='Пациент',
        default=True,
    )
    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='static/users/avatars',
        default='static/users/avatars/no_photo.jpg',
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.username})

    def save(self, *args, **kwargs):
        if self.is_patient:
            Patient.objects.get_or_create(profile_patient__id=self.id)
        super().save(*args, **kwargs)


class Patient(UserModelFieldsMixin):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.SET_NULL,
        verbose_name='Профиль пациента',
        related_name='patient_profile',
        blank=True, null=True,
    )
    insurance_policy = models.CharField(
        verbose_name='Страховой полис',
        blank=True, null=True,
        unique=True,
        max_length=16,
    )
    insurance_number_personal_account = models.CharField(
        verbose_name='СНИЛС',
        blank=True, null=True,
        unique=True,
        max_length=11,
    )
    birthdate = models.DateField(
        verbose_name='Дата рождения',
        blank=True, null=True
    )
    residential_address = models.CharField(
        verbose_name='Адрес проживания',
        blank=True, null=True,
        max_length=250,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        unique=True,
        blank=True, null=True,
        max_length=20
    )
    is_confirmed = models.BooleanField(
        verbose_name='Данные подтверждены',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        default=timezone.now,
    )

    def save(self, *args, **kwargs):
        # if self.profile:
        #     self.last_name = self.profile.last_name
        #     self.first_name = self.profile.first_name
        #     self.patronymic = self.profile.patronymic
        return super().save(*args, **kwargs)

    def __str__(self):
        if self.last_name:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        return str(self.id)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Doctor(UserModelFieldsMixin):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        verbose_name='Профиль врача',
        related_name='doctor_profile',
        blank=True, null=True
    )
    specialty = models.CharField(
        verbose_name='Специальность',
        max_length=100,
    )
    work_experience = models.CharField(
        verbose_name='Опыт работы',
        max_length=20,
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def save(self, *args, **kwargs):
        # if self.profile:
        #     self.last_name = self.profile.last_name
        #     self.first_name = self.profile.first_name
        #     self.patronymic = self.profile.patronymic
        return super().save(*args, **kwargs)


class MailDomains(models.Model):
    name_mail = models.CharField(max_length=150)
    domain = models.CharField(max_length=15)
    url = models.URLField()

    def __str__(self):
        return self.domain
