from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from .forms import UserCreationForm, LoginForm, TutorCreationForm
from .models import User


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('You have registered an account.'))
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def signup_tutor(request):
    if request.method == 'POST':
        form = TutorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, _('You have registered an account.'))
            return redirect('login')
    else:
        form = TutorCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup_tutor.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, _('You have logged in.'))
            return redirect('/')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, _('You have logged out.'))
    return redirect('/')


def search_tutor(request):
    context = {
        'tutors': User.get_tutors(),
    }
    return render(request, 'tutor_search.html', context)


def faq(request):
    return render(request, 'faq.html')
