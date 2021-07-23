from rest_framework import serializers
from WebApp.models import Teacher, Web, Course, Cost


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'
