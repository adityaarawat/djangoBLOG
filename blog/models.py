from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    category_name=models.CharField(max_length=250,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='categories'
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published")
)

class blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150, unique=True, blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class about(models.Model):
    about=models.CharField(max_length=25)
    about_description=models.TextField(max_length=450,default="Default description")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about


class social_links(models.Model):
    platform=models.CharField(max_length=30)
    link=models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform


class comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey(blog, on_delete=models.CASCADE)
    comment=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
