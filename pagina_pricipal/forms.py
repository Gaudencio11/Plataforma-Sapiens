
from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.shortcuts import redirect

from allauth.account  import views


           

class CustomSignupForm(SignupForm):
    #Usamos aqui a coluna 'lastname' do allauth para introduzirmos o CURSO do usuário


    last_name = forms.CharField(max_length=200, label='curso', widget=forms.TextInput(attrs={"placeholder": "curso"}),)

    
 
    


    def save(self, request):

        user = super(CustomSignupForm, self).save(request)

        return user

        

            