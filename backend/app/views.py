from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Notice

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
    contents = Notice.objects.filter()
    # user_id = request.session.get("user")
    # if user_id:
    #     user = User.objects.get(pk=user_id)
    #     return HttpResponse(f'{user} login success')
    return render(request, 'frontend/notice.html', {'contents':contents})

def login(request):
    u = request.user
    print(u)
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
        if str(u) == "AnonymousUser":
            print(str(u))
            return render(request, 'frontend/login.html')
        else:
            message = "로그인 할 수 없습니다."
            return home2(request, message)
        # return redirect("/")

def home2(request, message):
    print(message)
    contents = Notice.objects.filter()
    # user_id = request.session.get("user")
    # if user_id:
    #     user = User.objects.get(pk=user_id)
    #     return HttpResponse(f'{user} login success')
    return render(request, 'frontend/notice.html', {'contents':contents, 'message':message})

def logout(request):
    auth.logout(request)
    return redirect("/")

def write(request):
    if request.method == "POST":
        t = request.POST["title"]
        c = request.POST["board"]
        u = request.user
        print(u)
        Notice.objects.create(title=t, content=c, username=u.username)
        return redirect("/")
    else:
        u = request.user
        return render(request, 'frontend/writer.html', {'user':u})

def update(request, pk):
    contents = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        contents.title = request.POST["title"]
        contents.content = request.POST["board"]
        contents.save()
        return redirect("/")
    else:
        return render(request, 'frontend/update.html', {'contents':contents})

def delete(request, pk):
    if request.method == "POST":
        Notice.objects.get(pk=pk).delete()
        return redirect("/")