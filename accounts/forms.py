from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import User 

# login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).count() == 0:
            raise forms.ValidationError('Invalid username')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and User.objects.filter(password=password).count() == 0:
            raise forms.ValidationError('Invalid password')
        return password

# register form
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    birth_date = forms.DateField(label='Birth Date')

    # Clean the username.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('Username already exists')
        return username
    
    # Clean the email.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('Email already exists')
        return email
    
    # Clean the password.
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and User.objects.filter(password=password).count() > 0:
            raise forms.ValidationError('Password already exists')
        return password
    
    # Clean the first name.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and User.objects.filter(first_name=first_name).count() > 0:
            raise forms.ValidationError('First name already exists')
        return first_name
    
    # Clean the last name.
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and User.objects.filter(last_name=last_name).count() > 0:
            raise forms.ValidationError('Last name already exists')
        return last_name
    
    # Save the user.
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password'),
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
        )
        user.save()
        return user