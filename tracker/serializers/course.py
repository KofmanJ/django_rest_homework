from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from tracker.models import Course, Lesson
from tracker.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    # lessons = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Lesson.objects.all())

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons']
