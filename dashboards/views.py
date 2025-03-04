from django.shortcuts import render,redirect,get_object_or_404
from blog.models import category,blog
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import categoryAdd,BlogsAdd
from django.template.defaultfilters import slugify

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

def addBlog(request):
    form=blog.objects.all()
    context={
        'forms':form
    }
    return render(request,'dashboard/post.html',context)

def addPosts(request):
    if request.method == 'POST':
        form = BlogsAdd(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.author = request.user  # Assign the logged-in user

            # Generate slug
            base_slug = slugify(form.cleaned_data['title'])
            slug = base_slug
            counter = 1

            # Ensure the slug is unique
            while blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            post.slug = slug  # Assign the final slug
            post.save()  # Save the post with the slug

            return redirect('post')  # Redirect after successful form submission

    else:
        form = BlogsAdd()
    
    context = {'forms': form}
    return render(request, 'dashboard/add_posts.html', context)

def edit_post(request,pk):
    post=get_object_or_404(blog,pk=pk)
    if request.method=="POST":
        form=BlogsAdd(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('post')
    form=BlogsAdd(instance=post)
    context={
        'forms':form,
        'post':post
    }
    return render(request,'dashboard/edit_post.html',context)

def delete_post(request,pk):
    form=get_object_or_404(blog,pk=pk)
    form.delete()
    return redirect('post')