from django import forms
from home.models import Product, Category, User
from django.contrib.auth.forms import UserCreationForm
import re


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the Product Name'
    }))
    description = forms.CharField(label='Product Details',widget= forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the Product Details'
    }))
    image = forms.ImageField(label='Product Image', widget =forms.ClearableFileInput(attrs={
        'class': 'form-control',        
    }))
    category = forms.ModelChoiceField(label='Category Name',queryset=Category.objects.all(),widget=forms.Select(attrs={
            'class': 'form-control',
        }))
    price =forms.IntegerField(label ='Rate',widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the Rate of Product'
    }))
    stock =forms.IntegerField(label ='Quantity Available',widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the Quantity'
    }))
    class Meta:
        model = Product
        fields ='__all__'       
        # fields =['name','description']
        # exclude = ['stock']
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if len(name) < 10:
    #         return self.add_error('name','The product name must atleast have 10 characters')
    #     if not re.search('[0-9]',name):
    #         return self.add_error('name','The product name must atleast have 1 digit')
    #     if not re.search('[a-z]',name):
    #         return self.add_error('name','The product name must atleast have 1 alphabet')
    #     if not re.search('[A-Z]',name):
    #         return self.add_error('name','The product name must atleast have 1 capitalletter')

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the Category Name'

    }))
    class Meta:
        model = Category
        fields = '__all__'
        
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your First Name'
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Last Name'
    }))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Userame'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email address'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-enter your password'
    }))

    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                               max_length=100,
                               required=True, 
                               widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter your username'
    }))
    password = forms.CharField(label='Password',
                               max_length=100,
                               required=True, 
                               widget=forms.PasswordInput(attrs={
        'class':'form-control','placeholder':'Enter your password'
    }))