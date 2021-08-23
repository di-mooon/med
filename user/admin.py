from .models import ProfilePatient, ProfileDoctor, UserToken
from django.contrib import admin

admin.site.register(ProfilePatient)
admin.site.register(ProfileDoctor)
admin.site.register(UserToken)


