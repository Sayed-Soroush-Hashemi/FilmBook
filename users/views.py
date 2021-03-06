from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth import authenticate

from .models import FBUser
from .forms import RegisterationModelForm, EditProfileModelForm


def user_login(request):
    if request.user.is_authenticated():
        return redirect(reverse('user_edit_profile'))
    if request.method == "GET":
        return render(request, 'user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect(reverse('user_login') + "?login=fail")
        auth.login(request, user)
        return redirect(reverse('user_edit_profile') + "?login=success")


def user_logout(request):
    if request.user.is_anonymous():
        return redirect(reverse('user_login'))
    auth.logout(request)
    return redirect(reverse('user_login') + "?logout=success")


def user_register(request):
    if request.user.is_authenticated():
        return redirect(reverse('user_edit_profile'))
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
    if request.user.is_anonymous():
        return redirect(reverse('user_login'))
    print(request.user.username)
    request.user = FBUser.objects.get(username=request.user.username)
    if request.method == "GET":
        context = {
            'form': EditProfileModelForm(instance=request.user),
        }
        return render(request, 'edit_profile.html', context)
    if request.method == "POST":
        print("here3")
        form = EditProfileModelForm(instance=request.user, data=request.POST)
        if form.is_valid():
            print("here2")
            form.save(commit=True)
            context = {
                'form': form,
            }
            return render(request, 'edit_profile.html', context)
        else:
            context = {
                'form': form,
            }
            return render(request, 'edit_profile.html', context)
