from rest_framework import serializers

from .models import Tutor, Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):

    animals = AnimalSerializer(required=False, many=True)

    class Meta:
        model = Tutor
        exclude = ['password']


class AnimalSaleSerializer(serializers.Serializer):
    tutor = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all())