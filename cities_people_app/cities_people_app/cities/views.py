from django.http import HttpResponse
from django.shortcuts import render, redirect

from untitled1.cities.models import Person


def index(req):
    context = {
        'name': 'Doncho',
        'people': Person.objects.all()
    }
    return render(req, 'index.html', context)


def create_person(req):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia',
    ).save()

    return redirect('/cities')


def list_phones(request):
    #return HttpResponse('Phones list')
    context = {
        'phones': [
            {
                'name': 'Galaxy S5000',
                'quantity': 3,
            },
            {
                'name': 'Xiaomi Readmi T9',
                'quantity': 4,
            },
            {
                'name': 'iPhone 12',
                'quantity': 0,
            },
        ]
    }

    context['message'] = 'Phones list'
    return render(request, 'phones.html', context)
