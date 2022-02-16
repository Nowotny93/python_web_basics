from django.db import models

from todos_app.todos.forms import validate_dot


class Category(models.Model):

    HOME_CHOICE = 'Home'
    WORK_CHOICE = 'Work'
    NAME_CHOICES = (
        (HOME_CHOICE, 'Home stuff'),
        (WORK_CHOICE, 'Work stuff'),
    )

    text = models.CharField(max_length=30, choices=NAME_CHOICES)

    class Meta:
        verbose_name_plural = 'categories'


class Person(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'people'


class Todo(models.Model):
    title = models.CharField(max_length=30, validators=(
        validate_dot)
                             )
    state = models.BooleanField(default=False)
    description = models.TextField(null=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)
