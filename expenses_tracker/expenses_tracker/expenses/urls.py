from turtle import home

from django.urls import path

from expenses_tracker.expenses.views import home, create_expense, edit_expense, delete_expense

urlpatterns = (
    # Index
    path('', home, name='home'),

    # Expenses
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
)