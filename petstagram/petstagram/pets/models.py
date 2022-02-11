from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
    )

    type = models.CharField(max_length=6, choices=PET_TYPES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.id}; {self.name}; {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null='False')
