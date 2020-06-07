'''from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)

	class Meta:
		model=User
		fields=(
			'email',
			'password',
			)
	def save(self,commit=True):
		user=(RegistrationForm,self).save(commit=False)
		user.email=self.cleaned_data['email']
		if commit:
			user.save()

	#def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
		'''


import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,get_user_model, login, logout
#from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', required=True, max_length=50, widget=forms.TextInput(attrs={'type': 'text', 'name': 'username', 'class': 'form-control input-lg', 'placeholder': 'User Name'}))
	#email = forms.CharField(label='Email', required=True, max_length=50, widget=forms.EmailInput(attrs={'type':'email', 'name':'email', 'class': 'form-control', 'placeholder': 'Email Address'}))
	password = forms.CharField(label='Password', required=True, max_length=30, widget=forms.PasswordInput(attrs={'type': 'password', 'name':'password1', 'class': 'form-control','placeholder':'Password'}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data['username']
		#email = self.cleaned_data.get(.lower()
		password = self.cleaned_data['password']
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise ValidationError("Please enter a valid Username  and password!")
		return super(LoginForm, self).clean(*args, **kwargs)


class RegistrationForm(forms.Form):
	username = forms.CharField(label='', required=True, max_length=50,widget=forms.TextInput(attrs={'type': 'text', 'name':'username', 'class': 'form-control input-lg', 'placeholder': 'User Name'}))
	email = forms.EmailField(label='', required=True, max_length=30, widget=forms.EmailInput(attrs={'type':'email','name':'email', 'class': 'form-control input-lg', 'placeholder': 'Email'}))
	password1 = forms.CharField(required=True, max_length=30, label='',widget=forms.PasswordInput(attrs={'type': 'password', 'name':'password1', 'class': 'form-control input-lg','placeholder':'Password'}))
	password2 = forms.CharField(required=True, max_length=30, label='',widget=forms.PasswordInput(attrs={'type': 'password', 'name':'password2', 'class': 'form-control input-lg','placeholder': 'Confirm Password'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', ]


	def clean_username(self):
		user_name=self.cleaned_data['username']
		r = User.objects.filter(username=user_name)
		if r.count():
			raise ValidationError("User Name already exists")
		return user_name


	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise ValidationError("Email already exists")
		return email

	def clean_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
		raise ValidationError('Passwords do not match.')