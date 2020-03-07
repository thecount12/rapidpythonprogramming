#forms.py
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm): 
	birthdate = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	class Meta: 
		model = User 
		fields = ('username', 'birthdate', 'password1', 'password2', )
