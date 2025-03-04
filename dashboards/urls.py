from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    #categories Crud PAth
    path('category/',views.edit_categories,name='category'),
    path('add_category/',views.add_categories,name='Addcategory'),
    path("edit_category/<int:pk>/",views.edited_categories,name='editing'),
    path('del_category/<int:pk>',views.del_category,name='deleted'),
    #Blog Crud PAth
    path('post/',views.addBlog,name='post'),
    path('addPosts/',views.addPosts,name='addPosts'),
    path('edit_post/<int:pk>/',views.edit_post,name='edit_post'),
    path('delete_post/<int:pk>/',views.delete_post,name='delete')
]