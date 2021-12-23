from rest_framework import serializers

from .models import Lesson, StudentQuiz

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields='__all__'

