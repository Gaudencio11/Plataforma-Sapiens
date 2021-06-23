
from allauth.account.forms import SignupForm
from allauth.account.forms import EmailAddress

from django import forms
from .models import *
from django.shortcuts import redirect

from allauth.account  import views


           

class CustomSignupForm(SignupForm):
    #Usamos aqui a coluna 'lastname' do allauth para introduzirmos o CURSO do usuário


    last_name = forms.CharField(max_length=200, label='Curso', widget=forms.TextInput(attrs={"placeholder": "Curso"}),)
    first_name = forms.CharField(max_length=200, label='Nome', widget=forms.TextInput(attrs={"placeholder": "Nome"}),)
    email = forms.CharField(max_length=200, label='E-mail DASDASDASDA: ', widget=forms.TextInput(attrs={"placeholder": "Email INSTITUCIONAL"}),)
    
    


    def save(self, request):

        user = super(CustomSignupForm, self).save(request)

        return user

        

            