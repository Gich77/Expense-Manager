from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category', 'user')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description', 'user__username')


# Register your models here.
