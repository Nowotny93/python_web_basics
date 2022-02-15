from django.urls import path

from untitled1.cities.views import index, list_phones, create_person

urlpatterns = [
    path('', index),
    path('create/', create_person, name='create person'),
    path('phones/', list_phones)
]
