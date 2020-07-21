from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as lgin
from django.contrib.auth import logout as lgout
from django.urls import reverse_lazy


def login(request):
    """
    登录
    """
    if request.method == 'GET' and not request.user.is_authenticated:
        return render(request, 'login.html')
    # else:
    #     redirect(reverse_lazy('cms:cms'))
    # 提交的登陆post
    username = request.POST.get('user')
    pwd = request.POST.get('pwd', '')
    # 进行账号认证
    user = authenticate(username=username, password=pwd)
    # user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not user:  # 没有这个用户
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    lgin(request, user)
    return redirect('/')


@login_required(login_url=reverse_lazy('users:login'))
def logout(request):
    lgout(request)
    return redirect(reverse_lazy('users:login'))
