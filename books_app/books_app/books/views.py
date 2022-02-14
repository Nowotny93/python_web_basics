from django import forms
from django.shortcuts import render, redirect

from books_app.books.forms import BookForm
from books_app.books.models import Book


def show_create_form(request, form):
    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def index(request):
    context = {
        'books': Book.objects.all(),
    }

    return render(request, 'index.html', context)


def create_book(request):
    if request.method == 'GET':
        return show_create_form(request, BookForm())

    else:

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_create_form(request, form)


def show_update_form(request, form):
    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(
            initial=book.__dict__,
        )
        return show_update_form(request, form)
    else:
        form = BookForm(
            request.POST,
            instance=book
        )
        if form.is_valid():
            form.save()
            return redirect('index')

        return show_update_form(request, form)

