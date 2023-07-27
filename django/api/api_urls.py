from django.urls import path
from . import api_views

urlpatterns = [
    path('teachers/', api_views.get_teachers),
    path('teachers/<int:id>', api_views.get_teacher_page),
    path('teachers/create/', api_views.create_teacher),
    path('students/', api_views.get_students),
    path('students/<int:id>', api_views.get_student_page),
    path('students/create/', api_views.create_student),
    path('grades/', api_views.get_grades),
    path('grade/create/', api_views.create_grade),
    path('grade/delete/<int:id>', api_views.delete_grade),
]