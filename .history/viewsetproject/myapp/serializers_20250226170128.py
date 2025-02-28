from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:                 # class Meta is used to define the metadata of the serializer. Meta should be defined inside the serializer class.
        model = Student
        fields = "__all__"
        
        
class         