from rest_framework import serializers

from api.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'id',
            'name',
            'age',
            'get_students',
            'get_subjects',
            'school_name',
        )
