from . import views
from django.urls import path
urlpatterns = [
    path('<int:category_id>/', views.categories, name='category')
]