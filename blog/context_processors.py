from .models import category , social_links
def get_context(request):
    cate=category.objects.all()
    return dict(cate=cate)


def get_social(request):
    social=social_links.objects.all()
    return dict(social=social)