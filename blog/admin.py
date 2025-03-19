from django.contrib import admin
from .models import category,blog,about,social_links,comment

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    list_display=['title','category','author','status','is_featured']
    search_fields=['id','title','category__category_name','status']
    list_editable=['is_featured']

class aboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=about.objects.all().count()
        if count ==0 :
            return True
        return False

admin.site.register(category)
admin.site.register(blog,blogAdmin)
admin.site.register(about,aboutAdmin)
admin.site.register(social_links)
admin.site.register(comment)