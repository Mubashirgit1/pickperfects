from django.shortcuts import render,get_object_or_404,redirect, reverse
from django.core.paginator import Paginator
from .models import Product
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__friendly_name__icontains=query) | Q(sku__icontains=query) | Q(tags__icontains=query) | Q(occasion__icontains=query) | Q(recipient__icontains=query) | Q(tags__icontains=query) | Q(occasion__icontains=query)      
            products = products.filter(queries)
    
            # Paginate products - 15 per page
            paginator = Paginator(products, 15)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)



    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)