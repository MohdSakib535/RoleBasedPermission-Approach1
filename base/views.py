# myapp/views.py

from rest_framework import generics
from .models import CustomUser, School, Attendance
from .serializers import (
    CustomUserSerializer, SchoolSerializer,AttendanceSerializer
)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from base.custompermission import custom_permission_data,custom_permission2





class CustomUserListCreateView(generics.ListCreateAPIView):
    permission_classes=[custom_permission2]
    authentication_classes=[BasicAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


from rest_framework import viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [custom_permission_data]

# class SchoolListCreateView(generics.ListCreateAPIView):
#     permission_classes=[custom_permission_data]
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer

# class SchoolRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [custom_permission_data]
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Attendance
from .serializers import AttendanceSerializer,AttendanceSerializer2

class AttendanceAPIView(APIView):
    permission_classes=[IsAuthenticated,custom_permission2]
    def get(self, request, pk=None):
        if pk:
            # Retrieve a specific attendance record
            try:
                attendance = Attendance.objects.get(pk=pk)
            except Attendance.DoesNotExist:
                raise Http404
            serializer = AttendanceSerializer(attendance)
            return Response(serializer.data)
        else:
            # List all attendance records
            attendances = Attendance.objects.all()
            serializer = AttendanceSerializer(attendances, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Create a new attendance record
        serializer = AttendanceSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update a specific attendance record
        try:
            attendance = Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            raise Http404
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a specific attendance record
        try:
            attendance = Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            raise Http404
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

