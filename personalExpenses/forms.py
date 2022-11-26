from django.forms import ModelForm
from .models import user, userExpense

class userCreationform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email']


class ExpenseForm(ModelForm):
    class Meta:
        model = userExpense
        fields = ['month', 'monthly_earning', 'monthly_expenses', 'monthly_savings']