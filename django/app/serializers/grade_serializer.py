from rest_framework import serializers

from app.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            'id',
            'value',
            'teacher_name',
            'student_name',
            'subject_name',
        )
