from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, ChoiceFilter

from .serializers import TutorSerializer, AnimalSerializer, AnimalSaleSerializer
from .models import Tutor, Animal


class AnimalFilter(FilterSet):
    status = ChoiceFilter(choices=Animal.STATUS)

    class Meta:
        model = Animal
        fields = ['status', 'id']


class TutorFilter(FilterSet):
    status = ChoiceFilter(choices=Tutor.STATUS)
    
    class Meta:
        model = Tutor
        fields = ['status', 'id']


class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()
    filterset_class = TutorFilter
    filter_backends = [DjangoFilterBackend]

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    filterset_class = AnimalFilter
    filter_backends = [DjangoFilterBackend]

    # POST localhost:8000/animals/1/sell/
    # {"tutor": 2}
    @action(methods=["POST"], detail=True)
    def sell(self, request, pk, *args, **kwargs):
        animal_sale = AnimalSaleSerializer(data=request.data)
        animal_sale.is_valid(raise_exception=True)

        animal = self.get_queryset().get(pk=pk)
        animal.tutor = animal_sale.validated_data['tutor']
        animal.status = Animal.SOLD
        animal.save()

        return Response(status=200)

