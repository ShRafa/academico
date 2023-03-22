from rest_framework import serializers

from app.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'name',
            'city',
        )