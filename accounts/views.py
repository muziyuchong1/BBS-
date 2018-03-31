from django.contrib.auth import login as auth_login #as 重命名避免与内置login冲突
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render,redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #
        if form.is_valid(): #如果表单有效,
            user = form.save() #则用该实例创建一个User实例
            auth_login(request,user) #创建的user作为参数传递给auth_login函数,手动验证用户
            return redirect('home') #然后将用户重定向到主页,保持程序的流程
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})