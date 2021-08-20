from django.contrib import admin

from appointment.models import Patient, Record, DateRecord, TimeRecord


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('card', 'time', 'date',)

@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    list_display = ('time',)
    list_filter = ("daterecord",'card')

admin.site.register(DateRecord)


