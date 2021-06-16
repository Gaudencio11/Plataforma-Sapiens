
from allauth.account.forms import SignupForm
from django import forms
from .models import *
from django.shortcuts import redirect

from allauth.account  import views


           

class CustomSignupForm(SignupForm):
    #Usamos aqui a coluna 'lastname' do allauth para introduzirmos o cpf do usuário
    #Ainda estamos no processo de entender como realizar a validação desse cpf a partir de um bd


    last_name = forms.CharField(max_length=11, label='Curso', widget=forms.TextInput(attrs={"placeholder": "curso"}),)
 
    def save(self, request):

        user = super(CustomSignupForm, self).save(request)

        return user

        

            