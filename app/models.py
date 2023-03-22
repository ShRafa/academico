from django.contrib.auth.models import User
from django.db import models


class School(models.Model):
    name = models.TextField(max_length=50)
    city = models.TextField(max_length=50)


class Subject(models.Model):
    name = models.TextField(max_length=50)


class Student(models.Model):
    name = models.TextField(max_length=50)
    age = models.PositiveBigIntegerField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(
        Subject, related_name='students', blank=True
    )

    def __str__(self):
        return f'Student {self.name}'

    def age_is_valid(self):
        return self.age is not None

    def get_teachers(self):
        return [
            {'name': teacher.name, 'age': teacher.age}
            for teacher in self.teachers.all()
        ]

    def get_subjects(self):
        return [{'name': subject.name} for subject in self.subjects.all()]


class Teacher(models.Model):
    name = models.TextField(max_length=50)
    age = models.PositiveBigIntegerField(default=18)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, null=True, blank=True
    )
    subjects = models.ManyToManyField(
        Subject, related_name='teachers', blank=True
    )
    students = models.ManyToManyField(
        Student, related_name='teachers', blank=True
    )

    def __str__(self):
        return f'Teacher {self.name}'

    def age_is_valid(self):
        return (self.age is not None) and (self.age > 18)

    def get_students(self):
        return [
            {'name': student.name, 'age': student.age}
            for student in self.students.all()
        ]

    def get_subjects(self):
        return [{'name': subject.name} for subject in self.subjects.all()]

    def school_name(self):
        return self.school.name


class Grade(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=4)
    created_by = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True
    )
    for_student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    for_subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True
    )

    def value_is_valid(self):
        return 0 <= self.value <= 10

    def teacher_name(self):
        return self.created_by.name

    def student_name(self):
        return self.for_student.name

    def subject_name(self):
        return self.for_subject.name
