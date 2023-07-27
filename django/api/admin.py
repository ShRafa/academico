from django.contrib import admin

from api.models import School, Student, Subject, Grade, Teacher

@admin.register(School)
class Schooladmin(admin.ModelAdmin):
    list_display = ["name", "city"]
    search_fields = ["name", "city"]
    list_filter = ["city"]
    

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class Subjectadmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class Gradeadmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class Teacheradmin(admin.ModelAdmin):
    pass


# Register your models here.
