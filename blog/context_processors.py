from .models import category
def get_context(request):
    cate=category.objects.all()
    return dict(cate=cate)