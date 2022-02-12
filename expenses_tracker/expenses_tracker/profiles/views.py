from django.shortcuts import render, redirect

from expenses_tracker.core.budget import calculate_budget_left
from expenses_tracker.core.profile import get_profile
from expenses_tracker.expenses.models import Expense
from expenses_tracker.profiles.forms import ProfileForm


def profile_info(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    profile.budget_left = calculate_budget_left(profile, expenses)

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }

        return render(request, 'home-no-profile.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': form,
        }

        return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }

        return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile info')

        context = {
            'form': form,
        }

        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        profile.delete()
        return redirect('home')
