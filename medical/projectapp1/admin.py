

# Register your models here.
from django.contrib import admin
from .models import Medicalstore
# Register your models here.
class MedicalstoreAdmin(admin.ModelAdmin):
    list_display=['Medicine','Brand','Price']


admin.site.register(Medicalstore,MedicalstoreAdmin)