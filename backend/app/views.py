from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def join(request):
    if request.method == "POST":
        name = request.POST['username']
        pw = request.POST['password']

        User.objects.create_user(username=name, password=pw)
        return redirect("/")
    else:
        return render(request, 'frontend/join.html', {'app':"안녕"})

def home(request):
    return render(request, 'frontend/notice.html')

def login(request):
    if request.method=="POST":
        name = request.POST['username']
        pw = request.POST['password']

        # user -> authenticate
        user = auth.authenticate(request, username=name, password=pw) #get

        if user is None:
            message = "아이디 또는 비밀번호가 없습니다."
            return render(request, 'frontend/login.html',{'message':message})
        else:
            auth.login(request, user) #로그인 -> 마이페이지
            return redirect("/")
    else:
        return render(request, 'frontend/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")