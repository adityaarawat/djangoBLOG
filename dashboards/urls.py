from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('category/',views.edit_categories,name='category'),
    path('add_category/',views.add_categories,name='Addcategory'),
    path("edit_category/<int:pk>/",views.edited_categories,name='editing'),
    path('del_category/<int:pk>',views.del_category,name='deleted')
]