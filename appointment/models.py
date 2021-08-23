from django.db import models
from django.contrib.auth.models import User
from homepage.models import Card
from user.models import ProfilePatient


class DateRecord(models.Model):
    date = models.DateField('Дата приема', blank=True, null=True)
    weekday = models.CharField(verbose_name='День недели', max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.date)


class Patient(models.Model):
    name = models.CharField('Ф.И.О', max_length=150, default='')
    email = models.EmailField()
    phone = models.CharField('Телефон', max_length=20)
    insurance = models.CharField('Страховой полис', max_length=20)
    time_record_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        ProfilePatient,
        on_delete=models.CASCADE,
        related_name='patient_record',
        verbose_name='User',
        blank=True, null=True
    )

    def delete(self, *args, **kwargs):
        time = TimeRecord.objects.filter(patient=self)
        time.update(recorded=False)
        super(Patient, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name


class TimeRecord(models.Model):
    time = models.TimeField('Время приема')
    daterecord = models.ForeignKey(
        DateRecord,
        on_delete=models.CASCADE,
        verbose_name='Дата приема',
        related_name='timerecord',
        blank=True,
        null=True
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        verbose_name='Врач',
        blank=True,
        null=True,
        related_name='card_time'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.SET_NULL,
        verbose_name='Пациент',
        blank=True,
        null=True,
        related_name='time_patient'
    )
    date_now = models.DateTimeField(auto_now_add=True)
    recorded = models.BooleanField(default=False)

    def __str__(self):
        return str(self.time)


class Record(models.Model):  # не используется
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='record')
    time = models.ForeignKey(TimeRecord, on_delete=models.CASCADE, related_name='record_time', blank=True, null=True)
    date = models.ForeignKey(DateRecord, on_delete=models.CASCADE, related_name='record_date', blank=True, null=True)

    def get_dt(self):
        return self.time, self.date
