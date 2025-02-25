class StudentSerializer(serializers.ModelSerializer):
    class Meta:                 # class Meta is used to define the metadata of the serializer. Meta should be defined inside the serializer class.
        model = Student
        fields = "__all__"