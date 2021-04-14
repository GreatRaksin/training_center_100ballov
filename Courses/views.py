from django.shortcuts import render, get_object_or_404
from .models import Course


# Create your views here.
def index(request):
    courses_list = Course.objects.order_by('name')
    return render(request, 'course/index.html', {'courses_list': courses_list})


def details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'course/details.html', {'course': course})