from django.db import models

from user.models import Patient, Doctor


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name='Врач',
        related_name='appointment_doctor',
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name='Пациент',
        related_name='appointment_patient',
    )
    date = models.DateField(verbose_name='Дата приема')
    time = models.TimeField(verbose_name='Время приема')

    def __str__(self):
        return f"Запись №{self.id}"

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
        constraints = [models.UniqueConstraint(fields=['date', 'time', 'doctor'], name='unique_appointment')]
