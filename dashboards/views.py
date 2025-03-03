from django.shortcuts import render,redirect,get_object_or_404
from blog.models import category,blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import categoryAdd
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    cate=category.objects.all().count
    blogs=blog.objects.all().count
    context={
        'catiCount':cate,
        'blogcount':blogs
    }
    return render(request,'dashboard/dashboard.html',context)

def edit_categories(request):
    return render(request,'dashboard/categories.html')

def add_categories(request):
    if request.method == 'POST':
        form=categoryAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form=categoryAdd()
    context={
        'forms':form
    }
    return render(request,'dashboard/add_categories.html',context)

def edited_categories(request,pk):
    categoryy=get_object_or_404(category,pk=pk)
    if request.method=='POST':
        form=categoryAdd(request.POST,instance=categoryy)
        if form.is_valid():
            form.save()
            return redirect('category')
    form=categoryAdd(instance=categoryy)
    context={
        'forms':form,
        'data':categoryy
    }
    return render(request,'dashboard/edit_categories.html',context)

def del_category(request,pk):
    categoryy=get_object_or_404(category,pk=pk)
    categoryy.delete()
    return redirect('category')