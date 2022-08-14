from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate 메소드는 존재하는 user이면 user객체를, 그렇지 않으면 None 리턴
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return redirect('login.html')
    # GET 요청이 들어오면 login form을 담고있는 html을 띄워줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
