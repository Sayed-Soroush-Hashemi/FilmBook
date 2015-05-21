from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth

from .models import FBUser
from .forms import RegisterationModelForm


def user_login(request):
    if request.method == "GET":
        return render(request, 'user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return redirect(reverse('user_login') + "?login=fail")
        auth.login(request, user)
        return redirect(reverse('home') + "?login=success")


def user_logout(request):
    auth.logout(request.user)
    return redirect(reverse('user_login') + "?logout=success")


def user_register(request):
    if request.method == "GET":
        context = {
            'form': RegisterationModelForm(),
        }
        return render(request, 'user_register.html', context)
    elif request.method == "POST":
        form = RegisterationModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect(reverse('user_login') + "?login=success")
        else:
            context = {
                'form': form
            }
            return render(request, 'user_login.html', context)


def edit_profile(request):
    pass