from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


# Create your views here.


def account_login(request):
    if request.user.is_authenticated:
        return redirect('HomePage')

    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('HomePage')
        else:
            form.add_error('username', 'نام کاربری نامعتبر است')

    context = {
        'login_form': form
    }
    return render(request, 'account/account_login.html', context)


def account_register(request):
    if request.user.is_authenticated:
        return redirect('HomePage')

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        ur_email = form.cleaned_data['email']
        User.objects.create_user(username=username, email=ur_email, password=password)
        return redirect('account:account_login')

    context = {
        'register_form': form
    }
    return render(request, 'account/account_register.html', context)


def account_logout(request):
    logout(request)
    context = {
        'message': 'logout :)'
    }
    return render(request, 'HomePage.html', context)
