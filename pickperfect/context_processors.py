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
            tag_value = str(tag)
            if tag_value not in seen_tags:
                seen_tags.add(tag_value)
                if isinstance(tag, (int, float)) or (isinstance(tag, str) and tag.isdigit()):
                    all_tags.append({"value": tag_value, "label": f"{tag_value}%"})
                else:
                    all_tags.append({"value": tag_value, "label": str(tag)})

        occasions = product.occasion or []
        for occasion in occasions:
            if occasion not in seen_occasions:
                seen_occasions.add(occasion)
                all_occasions.append(occasion)

    return {
        "global_tags": all_tags,
        "global_occasions": all_occasions,
    }


def breadcrumbs(request):
    """Build breadcrumb items dynamically from the request path."""
    breadcrumbs = []
    title = ""

    if request.path and request.path != '/':
        # Resolve the current view to support nicer names for detail pages.
        view_name = None
        if hasattr(request, 'resolver_match') and request.resolver_match:
            view_name = request.resolver_match.url_name

        if view_name == 'product_detail':
            try:
                from products.models import Product
                product = Product.objects.filter(pk=request.resolver_match.kwargs.get('product_id')).first()
            except Exception:
                product = None

            breadcrumbs.append({'name': 'Products', 'url': '/products/'})
            if product:
                breadcrumbs.append({'name': product.name, 'url': request.path})
                title = product.name
            else:
                breadcrumbs.append({'name': 'Product', 'url': request.path})
                title = 'Product'
            return {'breadcrumbs': breadcrumbs, 'breadcrumb_title': title}

        if view_name == 'checkout_success':
            breadcrumbs.append({'name': 'Checkout', 'url': '/checkout/'})
            breadcrumbs.append({'name': 'Success', 'url': request.path})
            return {'breadcrumbs': breadcrumbs, 'breadcrumb_title': 'Checkout Success'}

        # Generic breadcrumb generation from path segments.
        segments = [seg for seg in request.path.strip('/').split('/') if seg]
        accumulated = ''
        for index, segment in enumerate(segments):
            accumulated += f'/{segment}'
            label = segment.replace('-', ' ').replace('_', ' ').title()
            if index < len(segments) - 1:
                breadcrumbs.append({'name': label, 'url': f'{accumulated}/'})
            else:
                breadcrumbs.append({'name': label, 'url': request.path})
                title = label

        # Add filter details for products pages.
        if view_name == 'products':
            categories = request.GET.getlist('category')
            tags = request.GET.getlist('tags')
            occasions = request.GET.getlist('occasion') + request.GET.getlist('occasions')

            if categories:
                category_labels = [cat.replace('-', ' ').replace('_', ' ').title() for cat in categories]
                breadcrumbs.append({
                    'name': f"Category: {', '.join(category_labels)}",
                    'url': request.get_full_path(),
                })
                title = f"Products - {', '.join(category_labels)}"

            if tags:
                tag_labels = [tag.replace('-', ' ').replace('_', ' ').title() for tag in tags]
                breadcrumbs.append({
                    'name': f"Tags: {', '.join(tag_labels)}",
                    'url': request.get_full_path(),
                })
                title = f"Products - {', '.join(tag_labels)}"

            if occasions:
                occasion_labels = [occ.replace('-', ' ').replace('_', ' ').title() for occ in occasions]
                breadcrumbs.append({
                    'name': f"Occasion: {', '.join(occasion_labels)}",
                    'url': request.get_full_path(),
                })
                title = f"Products - {', '.join(occasion_labels)}"

    return {
        'breadcrumbs': breadcrumbs,
        'breadcrumb_title': title,
    }


