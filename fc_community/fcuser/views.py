from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .form import LoginForm

# Create your views here.


def home(request):
    user_id = request.session.get('user')
    fcuser = None
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)

    return render(request, 'home.html', {'fcuser': fcuser})


def logout(request):
    if request.session:
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        usermail = request.POST.get('usermail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and password and re_password and usermail):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(username=username,
                            usermail=usermail,
                            password=make_password(password))
            fcuser.save()

        return render(request, 'register.html', res_data)
