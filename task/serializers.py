from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import Person
class AddPersonSerializer(serializers.ModelSerializer):

    name = serializers.CharField()

    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Name cannot be a number.")
        return value

    class Meta:
        model = Person
        fields = "__all__"