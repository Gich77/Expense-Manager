from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    objects = None
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('UTILITIES', 'Utilities'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"

    class Meta:
        ordering = ['-date']


