from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from blogmain.forms import AddUserForm,EditUserForm

# Create your views here.
def getUser(request):
    users=User.objects.all()
    context={
        "users":users
    }
    return render(request,"dashboard/users.html",context)

def addUser(request):
    if request.method=="POST":
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/users/')
        else:
            print(form.errors)
    form=AddUserForm()
    context={
        'forms':form
    }
    return render(request,"dashboard/add_user.html",context)

def editUser(request,pk):
    data=get_object_or_404(User,pk=pk)
    if request.method=="POST":
        form=EditUserForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/users/')
    form=EditUserForm(instance=data)
    context={
        'forms':form,
        'user':data
    }
    return render(request,'dashboard/edit_user.html',context)

def deleteUser(request,pk):
    data=get_object_or_404(User,pk=pk)
    data.delete()
    return redirect('/dashboard/users/')