
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Student


@admin.register(Student)
class StudentAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'student_id',
        'group',
        'course',
        'status',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'middle_name',
        'student_id',
    )

    list_filter = (
        'group',
        'course',
        'status',
        'education_form',
        'funding',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Личные данные', {
            'fields': (
                'middle_name',
                'birth_date',
                'gender',
                'phone',
                'address',
                'photo',
            )
        }),
        ('Обучение', {
            'fields': (
                'student_id',
                'group',
                'course',
                'admission_year',
                'education_form',
                'funding',
                'status',
            )
        }),
    )
