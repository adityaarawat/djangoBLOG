from django.urls import path
from . import views
urlpatterns=[
path("",views.getUser,name="getUser"),
path('addUser/',views.addUser,name='addUser'),
path('editUser/<int:pk>/',views.editUser,name='editUser'),
path('deleteUser/<int:pk>/',views.deleteUser,name='deleteUser')
]