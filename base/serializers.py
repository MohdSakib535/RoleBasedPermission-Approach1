from rest_framework import serializers
from .models import CustomUser, School, Attendance

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class SchoolSerializer(serializers.ModelSerializer):
    principal = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='Principal'),
        required=False,  # Allow null if you want to create a School without assigning a principal initially
    )

    class Meta:
        model = School
        fields = '__all__'


class SchoolSerializer2(serializers.ModelField):
    class Meta:
        model=School
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    # user_Data=CustomUserSerializer()
    user_Data=serializers.StringRelatedField()
    class Meta:
        model = Attendance
        fields = '__all__'


class AttendanceSerializer2(serializers.ModelSerializer):
    user_Data=serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='Student'))
    class Meta:
        model = Attendance
        fields = '__all__'
