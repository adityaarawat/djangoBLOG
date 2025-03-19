from django.shortcuts import render
from .models import blog ,category,comment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

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
    if request.method=="POST":
        comments=comment()
        comments.user=request.user
        comments.blog=singleBlog
        comments.comment=request.POST['comment']
        comments.save()
        return HttpResponseRedirect(request.path_info)
    comments=comment.objects.filter(blog=singleBlog)
    commentsCount=comments.count()
    context={
        'singleBlog':singleBlog,
        'comments':comments,
        "commentsCount":commentsCount
    }
    return render(request,'blog.html',context)




def search(request):
    return render(request, 'search.html')  # Ensure 'search.html' exists in your templates folder







    