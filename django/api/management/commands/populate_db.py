from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from api.models import Grade, School, Student, Subject, Teacher


class Command(BaseCommand):
    help = 'Popula o banco para efetuar testes'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        if not User.objects.all().exists():
            User.objects.create_superuser(
                username='admin', email='admin@email.com', password='admin'
            )
            self.stdout.write(
                self.style.SUCCESS(
                    'Superuser successfully created! login: admin / password: admin'
                )
            )

        if not School.objects.all().exists():
            nathanael = School.objects.create(
                name='Nathanel Silva', city='Varzea Paulista'
            )
            tanaka = School.objects.create(
                name='Tanaka', city='Varzea Paulista'
            )
            divino = School.objects.create(name='Divino', city='Jundiai')
            self.stdout.write(
                self.style.SUCCESS('School successfully created!')
            )

        if not Subject.objects.all().exists():
            matematica = Subject.objects.create(name='Matematica')
            portugues = Subject.objects.create(name='Portugues')
            quimica = Subject.objects.create(name='Quimica')
            biologia = Subject.objects.create(name='Biologia')
            educacao_fisica = Subject.objects.create(name='Educacao Fisica')
            self.stdout.write(
                self.style.SUCCESS('Subjects successfully created!')
            )

        if not Student.objects.all().exists():
            student1 = Student.objects.create(
                name='Joao Vitor',
                age=14,
                school=nathanael,
            )
            student1.subjects.add(matematica, biologia, portugues)

            student2 = Student.objects.create(
                name='Rafael Silva',
                age=16,
                school=nathanael,
            )
            student2.subjects.add(matematica, portugues, biologia)

            student3 = Student.objects.create(
                name='Rafael Augusto',
                age=13,
                school=tanaka,
            )
            student3.subjects.add(matematica, portugues, biologia)

            student4 = Student.objects.create(
                name='Gustavo Pinho',
                age=15,
                school=tanaka,
            )
            student4.subjects.add(matematica, portugues, biologia)

            student5 = Student.objects.create(
                name='Fernando Albino',
                age=16,
                school=divino,
            )
            student5.subjects.add(quimica, educacao_fisica)

            student6 = Student.objects.create(
                name='Bruno Souza',
                age=16,
                school=divino,
            )
            student6.subjects.add(quimica, educacao_fisica)

            student7 = Student.objects.create(
                name='Ronaldo Pereira',
                age=17,
                school=nathanael,
            )
            student7.subjects.add(quimica, educacao_fisica)

            student8 = Student.objects.create(
                name='Maycon Douglas',
                age=12,
                school=nathanael,
            )
            student8.subjects.add(quimica, educacao_fisica)

            student9 = Student.objects.create(
                name='isabel Cristina',
                age=17,
                school=tanaka,
            )
            student9.subjects.add(
                matematica, portugues, biologia, quimica, educacao_fisica
            )

            student10 = Student.objects.create(
                name='Carol Barbiere',
                age=16,
                school=tanaka,
            )
            student10.subjects.add(
                matematica, portugues, biologia, quimica, educacao_fisica
            )

            student11 = Student.objects.create(
                name='Marcela Luiza',
                age=14,
                school=divino,
            )
            student11.subjects.add(
                matematica, portugues, biologia, quimica, educacao_fisica
            )

            student12 = Student.objects.create(
                name='Louise Piloto',
                age=14,
                school=divino,
            )
            student12.subjects.add(
                matematica, portugues, biologia, quimica, educacao_fisica
            )

            student13 = Student.objects.create(
                name='Natalia Souza',
                age=17,
                school=nathanael,
            )
            student13.subjects.add(
                matematica, portugues, biologia, quimica, educacao_fisica
            )
            self.stdout.write(
                self.style.SUCCESS('Students successfully created!')
            )

        if not Teacher.objects.all().exists():
            vitor_toledo = Teacher.objects.create(
                name='Vitor Toledo',
                age='21',
                school=nathanael,
            )
            vitor_toledo.subjects.add(matematica)
            vitor_toledo.students.add(student1, student2, student3, student4)

            diogo_benica = Teacher.objects.create(
                name='Diogo Benica',
                age='31',
                school=divino,
            )
            diogo_benica.subjects.add(portugues)
            diogo_benica.students.add(
                student1, student5, student6, student7, student8
            )

            charles_darwin = Teacher.objects.create(
                name='Charles Darwin',
                age='55',
                school=divino,
            )
            charles_darwin.subjects.add(biologia, educacao_fisica, quimica)
            charles_darwin.students.add(
                student1, student9, student10, student11, student12, student13
            )
            self.stdout.write(
                self.style.SUCCESS('Teachers successfully created!')
            )

        if not Grade.objects.all().exists():
            Grade.objects.create(
                value=8.00, created_by_id=1, for_student_id=1, for_subject_id=1
            )
            Grade.objects.create(
                value=3.00, created_by_id=2, for_student_id=2, for_subject_id=2
            )
            self.stdout.write(
                self.style.SUCCESS('Grade successfully created!')
            )
