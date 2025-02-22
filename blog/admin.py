from django.contrib import admin
from .models import categories,blog

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    list_display=['title','category','author','status','is_featured']
    search_fields=['id','title','category__category_name','status']
    list_editable=['is_featured']

admin.site.register(categories)
admin.site.register(blog,blogAdmin)