from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import Grade, Student, Teacher
from app.serializers.grade_serializer import GradeSerializer
from app.serializers.student_serializer import StudentSerializer
from app.serializers.teacher_serializer import TeacherSerializer


@csrf_exempt
def get_teachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)


@csrf_exempt
def get_teacher_page(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return JsonResponse({'error': 'Teacher does not exist'}, status=404)
    except:
        return JsonResponse({'error': 'undefined error'}, status=404)

    serializer = TeacherSerializer(teacher, many=False)
    return JsonResponse(serializer.data, status=200)


@csrf_exempt
def create_teacher(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'undefined method'}, status=404)

    name = request.POST['name']
    age = request.POST['age']
    school_id = request.POST['school_id']
    subjects = request.POST['subjects'].split(', ')
    students = request.POST['students'].split(', ')

    teacher = Teacher(name=name, age=age, school_id=school_id)
    if not teacher.age_is_valid():
        return JsonResponse(
            {'error': '{teacher.age} are too young'}, status=404
        )

    teacher.save()

    for subject in subjects:
        teacher.subjects.add(subject)

    for student in students:
        teacher.students.add(student)

    serializer = TeacherSerializer(teacher, many=False)
    return JsonResponse(serializer.data, status=201)


@csrf_exempt
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)


@csrf_exempt
def get_student_page(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student does not exist'}, status=404)
    except:
        return JsonResponse({'error': 'undefined error'}, status=404)

    serializer = StudentSerializer(student, many=False)
    return JsonResponse(serializer.data, status=200)


@csrf_exempt
def create_student(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'undefined method'}, status=404)

    name = request.POST['name']
    age = request.POST['age']
    school_id = request.POST['school_id']
    subjects = request.POST['subjects'].split(', ')
    teachers = request.POST['teachers'].split(', ')

    student = Student(name=name, age=age, school_id=school_id)
    if not student.age_is_valid():
        return JsonResponse(
            {'error': f'{student.age} age is not valid'}, status=404
        )

    student.save()

    for subject in subjects:
        student.subjects.add(subject)

    for teacher in teachers:
        student.teachers.add(teacher)

    serializer = StudentSerializer(student, many=False)
    return JsonResponse(serializer.data, status=201)


@csrf_exempt
def get_grades(request):
    grades = Grade.objects.all()
    serializer = GradeSerializer(grades, many=True)
    return JsonResponse(serializer.data, status=200, safe=False)


@csrf_exempt
def create_grade(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'undefined method'}, status=404)

    value = float(request.POST['value'])
    teacher_id = request.POST['teacher_id']
    student_id = request.POST['student_id']
    subject_id = request.POST['subject_id']

    grade = Grade(
        value=value,
        created_by_id=teacher_id,
        for_student_id=student_id,
        for_subject_id=subject_id,
    )

    if not grade.value_is_valid():
        return JsonResponse(
            {'error': f'Grade {grade.grade} is not valid'}, status=404
        )

    grade.save()

    serializer = GradeSerializer(grade, many=False)
    return JsonResponse(serializer.data, status=201)


@csrf_exempt
def delete_grade(request, id):
    try:
        grade = Grade.objects.get(id=id)
    except Grade.DoesNotExist:
        return JsonResponse({'error': 'Grade does not exist'}, status=404)
    except:
        return JsonResponse({'error': 'undefined error'}, status=404)

    grade.delete()

    return JsonResponse({}, status=202)
