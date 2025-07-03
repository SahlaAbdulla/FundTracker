from django import forms
from expense.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class ExpenseCreateForm(forms.Form):
      
#     title = forms.CharField()

#     amount = forms.FloatField()

#     category = forms.ChoiceField(choices=Transaction.CATEGORY_OPTIONS)

#     payment_method = forms.ChoiceField(choices=Transaction.PAYMENT_OPTIONS)

#     priority = forms.ChoiceField(choices=Transaction.PRIORITY_OPTIONS)

class ExpenseCreateForm(forms.ModelForm):

    class Meta:

        model=Transaction

        fields=['title','amount','category','payment_method','priority']  

        widgets={
            
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control form-select"}),
            "payment_method":forms.Select(attrs={"class":"form-control form-select"}),
            "priority":forms.Select(attrs={"class":"form-control form-select mb-3"}),
        }  

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()   

    



