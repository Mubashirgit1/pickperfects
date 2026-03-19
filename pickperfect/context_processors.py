from django.db.models import Count
from products.models import Category
from products.models import Product


def nav_categories(request):
    categories = Category.objects.annotate(product_count=Count('product'))
    return {"nav_categories": categories}


def global_tags(request):
    all_tags = []
    all_occasions = []
    seen_tags = set()
    seen_occasions = set()

    for product in Product.objects.all():
        tags = product.tags or []
        for tag in tags:
            if tag not in seen_tags:
                seen_tags.add(tag)
                all_tags.append(tag)

        occasions = product.occasion or []
        for occasion in occasions:
            if occasion not in seen_occasions:
                seen_occasions.add(occasion)
                all_occasions.append(occasion)

    return {
        "global_tags": all_tags,
        "global_occasions": all_occasions,
    }


