from django.db import models

# Create your models here.
from django.db import models


class Faculty(models.Model):
    name = models.CharField(
        "Название факультета",
        max_length=200,
        unique=True,
    )
    short_name = models.CharField(
        "Сокращённое название",
        max_length=50,
        unique=True,
    )
    dean = models.CharField(
        "Декан",
        max_length=200,
    )

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"
        ordering = ["name"]

    def __str__(self):
        return self.short_name


class Direction(models.Model):
    code = models.CharField(
        "Код направления",
        max_length=20,
        unique=True,
    )
    name = models.CharField(
        "Название направления",
        max_length=200,
    )
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.PROTECT,
        related_name="directions",
        verbose_name="Факультет",
    )
    study_duration = models.PositiveSmallIntegerField(
        "Срок обучения (лет)",
    )

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class Group(models.Model):
    name = models.CharField(
        "Название группы",
        max_length=100,
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.PROTECT,
        related_name="groups",
        verbose_name="Направление",
    )
    admission_year = models.PositiveSmallIntegerField(
        "Год набора",
    )
    is_active = models.BooleanField(
        "Активна",
        default=True,
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["-admission_year", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "direction", "admission_year"],
                name="unique_group_direction_year",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.admission_year})"
