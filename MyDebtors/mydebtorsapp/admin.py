from django.contrib import admin
from .models import Student, School, Comment

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Comment)

