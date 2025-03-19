from django.shortcuts import render,redirect
from blog.models import about,blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth

def home(request):
    # categoryy=category.objects.all()
    blogs=blog.objects.filter(is_featured=True).order_by('updated_at')
    abouts=about.objects.get()
    featured=blog.objects.filter(status='Published',is_featured=False)
    context={
        'abouted':abouts,
        'blogs':blogs,
        'features':featured
    }
    return render(request,'home.html',context)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')

    else :
        form=RegistrationForm()

    context={
        'forms':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        login = AuthenticationForm(request,request.POST)
        if login.is_valid():
            username=login.cleaned_data['username']
            password=login.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    login=AuthenticationForm()
    context={
        'logins':login
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')


