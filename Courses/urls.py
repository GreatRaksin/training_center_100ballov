from django.urls import path

from . import views

app_name = 'Courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('specifics/<int:course_id>', views.details, name='details')
]