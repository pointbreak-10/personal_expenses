from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class userExpense(models.Model):
    MONTH_CHOICES=[
        ("JAN","January"),("FEB","February"),("MAR","March"),("APR","April"),("MAY","May"),("JUN","June"),("JUL","July"),("AUG","Aug"),
        ("SEP","September"),("OCT","October"),("NOV","November"),("DEC","December")]

    month = models.CharField(max_length=3, choices=MONTH_CHOICES, default="JAN", unique=True)
    monthly_expenses = models.IntegerField(default=0)
    monthly_earning = models.IntegerField(default=0)
    monthly_savings = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.month




