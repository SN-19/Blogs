
from .form import UserRegistrationForm,UserProfileForm,UserLoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from django.http import HttpResponseRedirect


def signup(request):
    if request.method == 'POST':
        profile = UserProfileForm(request.POST)
        user =UserRegistrationForm(request.POST,prefix='user')
        if profile.is_valid() and user.is_valid():
            username = user.cleaned_data.get('username')
            password1 = user.cleaned_data.get('password1')
            password2 = user.cleaned_data.get('password2')
            phone = profile.cleaned_data.get('phone')
            if password1 == password2:
                userdata = user.save()
                userdata.refresh_from_db()
                userdata.userprofile.phone = phone
                userdata.save()
                user = authenticate(username=username, password=password1)
                return HttpResponseRedirect('/index/')
    profile = UserProfileForm()
    user = UserRegistrationForm(prefix='user')
    return render(request,'user_signup.html',{'profileform':profile,'userform':user})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return  HttpResponseRedirect('/index/')
    user = UserLoginForm()
    return render(request,'user_login.html',{'form':user})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')