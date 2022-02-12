from django.shortcuts import render, redirect

from expenses_tracker.core.profile import get_profile
from expenses_tracker.expenses.forms import ExpenseForm, DeleteExpenseForm
from expenses_tracker.expenses.models import Expense


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    profile.budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'expenses': expenses,
        'budget': profile,
        'budget_left': profile,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'GET':
        context = {
            'form': ExpenseForm(),
        }

        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.profile = get_profile()
            expense.save()
            return redirect('home')

        context = {
            'form': form,
        }

        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }

        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'expense': expense,
            'form': form,
        }

        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpenseForm(instance=expense),
        }

        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('home')
