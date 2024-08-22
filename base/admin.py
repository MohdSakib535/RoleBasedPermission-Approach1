from django.contrib import admin
from .models import CustomUser,School,Attendance

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(School)
admin.site.register(Attendance)
