from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Doctor)
admin.site.register(Pharmacist)
admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(MedicalHistory)
admin.site.register(Permission)
