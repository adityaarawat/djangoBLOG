from django.shortcuts import render
from .models import blog ,category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.


def categories(request,category_id):
    blogs=blog.objects.filter(category_id=category_id)
    categories =get_object_or_404(category,pk=category_id)
    context={
            'blog':blogs,
            'category':categories
            }
    return render(request,'categories.html',context)



def blogs(request,slug):
    singleBlog=get_object_or_404(blog,slug=slug,status='Published')
    context={
        'singleBlog':singleBlog
    }
    return render(request,'blog.html',context)



def search_view(request):
    return HttpResponse("Working")
  
    