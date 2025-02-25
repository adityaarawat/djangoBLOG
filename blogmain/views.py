from django.shortcuts import render
from blog.models import category,blog

def home(request):
    # categoryy=category.objects.all()
    blogs=blog.objects.filter(is_featured=True).order_by('updated_at')
    featured=blog.objects.filter(status='Published',is_featured=False)
    context={
        # 'category':categoryy,
        'blogs':blogs,
        'features':featured
    }
    return render(request,'home.html',context)
