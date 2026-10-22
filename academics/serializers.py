from rest_framework import serializers

from .models import Faculty, Direction, Group


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            "id",
            "name",
            "short_name",
            "dean",
        ]
        read_only_fields = ["id"]


class DirectionSerializer(serializers.ModelSerializer):
    faculty_name = serializers.CharField(
        source="faculty.name",
        read_only=True,
    )

    class Meta:
        model = Direction
        fields = [
            "id",
            "code",
            "name",
            "faculty",
            "faculty_name",
            "study_duration",
        ]
        read_only_fields = ["id", "faculty_name"]


class GroupSerializer(serializers.ModelSerializer):
    direction_name = serializers.CharField(
        source="direction.name",
        read_only=True,
    )

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "direction",
            "direction_name",
            "admission_year",
            "is_active",
        ]
        read_only_fields = ["id", "direction_name"]
