from django.db.models import Count
from products.models import Category
from products.models import Product


def nav_categories(request):
    categories = Category.objects.annotate(product_count=Count('product'))
    return {"nav_categories": categories}


def global_tags(request):
    all_tags = []
    seen = set()

    for product in Product.objects.all():
        tags = product.tags or []
        for tag in tags:
            if tag not in seen:
                seen.add(tag)
                all_tags.append(tag)

    return {
        "global_tags": all_tags
    }


