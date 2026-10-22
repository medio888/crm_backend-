
from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    GENDER_CHOICES = [
        ("M", "Мужской"),
        ("F", "Женский"),
    ]

    EDUCATION_FORM_CHOICES = [
        ("full_time", "Очная"),
        ("part_time", "Заочная"),
    ]

    FUNDING_CHOICES = [
        ("budget", "Бюджет"),
        ("contract", "Контракт"),
    ]

    STATUS_CHOICES = [
        ("studying", "Обучается"),
        ("academic_leave", "Академический отпуск"),
        ("expelled", "Отчислен"),
        ("graduated", "Выпустился"),
    ]

    # Личные данные
    middle_name = models.CharField(
        "Отчество",
        max_length=150,
        blank=True,
    )

    birth_date = models.DateField(
        "Дата рождения",
        null=True,
        blank=True,
    )

    gender = models.CharField(
        "Пол",
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
    )

    phone = models.CharField(
        "Телефон",
        max_length=20,
        blank=True,
    )

    address = models.CharField(
        "Адрес",
        max_length=255,
        blank=True,
    )

    photo = models.ImageField(
        "Фотография",
        upload_to="students/",
        null=True,
        blank=True,
    )

    # Данные студента
    student_id = models.CharField(
        "Номер студенческого билета",
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )

    group = models.ForeignKey(
        "academics.Group",
        on_delete=models.PROTECT,
        related_name="students",
        verbose_name="Группа",
        null=True,
        blank=True,
    )


    course = models.PositiveSmallIntegerField(
        "Курс",
        choices=[
            (1, "1 курс"),
            (2, "2 курс"),
            (3, "3 курс"),
            (4, "4 курс"),
        ],
        null=True,
        blank=True,
    )

    admission_year = models.PositiveSmallIntegerField(
        "Год поступления",
        null=True,
        blank=True,
    )

    education_form = models.CharField(
        "Форма обучения",
        max_length=20,
        choices=EDUCATION_FORM_CHOICES,
        blank=True,
    )

    funding = models.CharField(
        "Финансирование",
        max_length=20,
        choices=FUNDING_CHOICES,
        blank=True,
    )

    status = models.CharField(
        "Статус студента",
        max_length=20,
        choices=STATUS_CHOICES,
        default="studying",
    )

    # Даты создания и изменения
    created_at = models.DateTimeField(
        "Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        "Дата обновления",
        auto_now=True,
    )

    # При создании суперпользователя спрашивать только username
    # и password (с повторным подтверждением пароля).
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.last_name} {self.first_name}".strip()

        return self.username

    @property
    def full_name(self):
        return " ".join(
            part
            for part in [
                self.last_name,
                self.first_name,
                self.middle_name,
            ]
            if part
        )
