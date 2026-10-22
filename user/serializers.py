
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    group_name = serializers.SerializerMethodField()

    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "full_name",
            "email",
            "birth_date",
            "gender",
            "phone",
            "address",
            "photo",
            "student_id",
            "group",
            "group_name",
            "course",
            "admission_year",
            "education_form",
            "funding",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "full_name",
            "group_name",
            "created_at",
            "updated_at",
        ]

    def get_group_name(self, obj):
        return obj.group.name if obj.group else None

    def create(self, validated_data):
        password = validated_data.pop("password")
        student = Student(**validated_data)
        student.set_password(password)
        student.save()
        return student

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
