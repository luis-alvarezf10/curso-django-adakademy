from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = '/'
    form_class = UserCreationForm

