from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm

import logging

logger = logging.getLogger(__name__)

def home(req): 
    return render(req, 'base.html')

def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('expense_list')  # Redirect to the expense list page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_expense(request):
    """Handle expense creation."""
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Associate expense with the logged-in user
            expense.save()
            messages.success(request, "Expense added successfully!")
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/create_expense.html', {'form': form})

@login_required
def expense_list(request):
    """Display a paginated list of the user's expenses."""
    expenses = Expense.objects.filter(user=request.user).order_by('-date')  # Latest expenses first
    paginator = Paginator(expenses, 5)  # Show 5 expenses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expenses/expense_list.html', {'page_obj': page_obj})


@login_required
def update_expense(request, expense_id):
    """Handle expense updates."""
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated successfully!")
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/update_expense.html', {'form': form})


@login_required
def delete_expense(request, expense_id):
    """Handle expense deletion."""
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, "Expense deleted successfully!")
        return redirect('expense_list')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})
