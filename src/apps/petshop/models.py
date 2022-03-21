from django.db import models

from encrypted_model_fields.fields import EncryptedCharField

from apps.utils.models import LogicDeletionModel


class Tutor(LogicDeletionModel):
    
    ACTIVE = 'Acti'
    INACTIVE = 'Inac'

    STATUS = [
        (ACTIVE, 'Ativo'),
        (INACTIVE, 'Inativo'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = EncryptedCharField(max_length=255)
    phone = models.CharField(max_length=11)
    status = models.CharField(
        max_length=4,
        choices=STATUS,
        default=None,
    )


class Animal(LogicDeletionModel):

    DOG = 'DOG'
    CAT = 'CAT'

    TYPE = [
        (DOG, 'Cachorro'),
        (CAT, 'Gato'),
    ]

    ACTIVE = 'ACTI'
    PENDING = 'PEND'
    SOLD = 'SOLD'

    STATUS = [
        (ACTIVE, 'Ativo'),
        (PENDING, 'Pendente'),
        (SOLD, 'Vendido'),
    ]

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    type = models.CharField(
        max_length=3,
        choices=TYPE,
        default=None,
    )

    breed = models.CharField(max_length=255)
    status = models.CharField(
        max_length=4,
        choices=STATUS,
        default=None,
    )

    tutor = models.ForeignKey(to=Tutor, related_name="animals", on_delete=models.CASCADE, null=True)