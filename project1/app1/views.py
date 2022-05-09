from functools import partial
from django.shortcuts import render
from .models import Student
from app1.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class StudentDetails(viewsets.ViewSet):
    def list(self,request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create (self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
             std = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'msg':'Record does not Found'})
        serializer = StudentSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            std = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'msg':'Recored  dose not Found '})
        serializer = StudentSerializer(std)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy (self, request, pk):
        try:
            std = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'msg':'Record does not found'})
        std.delete()
        return Response({'msg':'Record deleted successfully'})

