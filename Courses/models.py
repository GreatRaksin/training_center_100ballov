from django.db import models
from datetime import datetime


# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Teachers(models.Model):
    name = models.CharField(max_length=150, unique=True)
    photo = models.ImageField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField('Дата проведения')
    seats = models.IntegerField(default=1)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
