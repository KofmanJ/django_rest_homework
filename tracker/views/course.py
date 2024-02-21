from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from tracker.models import Course
from tracker.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
