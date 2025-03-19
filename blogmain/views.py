from django.shortcuts import render,redirect
from blog.models import about,blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.contrib import messages
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

# views.py

def email(request):
    return render(request,'email_form.html')


from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Include user's email in the body (not as the sender)
        full_message = f"From: {name} <{user_email}>\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                'aadityarawatt@gmail.com',  
                ['aadityarawatt@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent!')
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

        return redirect('send_email')  # Reload the form

    return render(request, 'email_form.html')


