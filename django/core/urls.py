from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/', views.get_teachers),
    path('teachers/<int:id>', views.get_teacher_page),
    path('teachers/create/', views.create_teacher),
    path('students/', views.get_students),
    path('students/<int:id>', views.get_student_page),
    path('students/create/', views.create_student),
    path('grades/', views.get_grades),
    path('grade/create/', views.create_grade),
    path('grade/delete/<int:id>', views.delete_grade),
]
