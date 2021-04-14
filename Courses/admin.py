from django.contrib import admin
from .models import Teachers, Student, Cities, Course


# Register your models here.
admin.site.register(Teachers)
admin.site.register(Student)
admin.site.register(Cities)
admin.site.register(Course)