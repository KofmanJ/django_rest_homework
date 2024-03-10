from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField

from tracker.models import Course, Subscription
from tracker.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    # lesson = LessonSerializer(many=True, read_only=True, source='lessons')
    lessons = LessonSerializer(many=True, read_only=True)
    # lessons = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Lesson.objects.all())
    is_subscribed = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lesson_count', 'lessons', 'is_subscribed']
