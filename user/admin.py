from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Profile, MailDomains, Doctor, Patient


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    model = Profile
    add_fieldsets = ((None, {'classes': ('wide',),
                             'fields': ('username', 'email', 'password1', 'password2', 'is_doctor', 'is_patient'), }),)
    fieldsets = (('Персональная информация', {'fields': ('username', 'password', 'email', 'avatar')}),
                 ('Важные даты ', {'fields': ('date_joined', 'last_login')}),
                 ('Права доступа', {'fields': (
                     'is_active', 'is_patient', 'is_doctor',
                     'is_staff', 'is_superuser', 'groups', 'user_permissions')}))


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # list_display = ('id', 'profile_patient',)
    # fields = ('profile_patient',)
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(MailDomains)
