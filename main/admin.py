from django.contrib import admin
from .models import AbsenceType, Log, Student, Grade, Board
# Register your models here.

admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Board)
admin.site.register(Log)
admin.site.register(AbsenceType)