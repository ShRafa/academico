from django.contrib import admin

from app.models import Grade, School, Student, Subject, Teacher


admin.site.register(Grade)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)