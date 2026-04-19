from django.shortcuts import render,get_object_or_404,redirect, reverse
from django.core.paginator import Paginator
from .models import Product,Category
from django.db.models import Q
from django.contrib import messages
from .forms import ProductForm
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    tags = None
    current_tags =None
    current_occasions = None
    f_products = None
    sale_products = None
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))           
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__friendly_name__icontains=query) | Q(sku__icontains=query) | Q(tags__icontains=query) | Q(occasion__icontains=query) | Q(recipient__icontains=query)      
            products = products.filter(queries)
        if 'tags' in request.GET:
            tags = request.GET.getlist('tags')
            current_tags = tags
            tag_queries = Q()
            for tag in tags:
                tag_queries |= Q(tags__icontains=tag)
            products = products.filter(tag_queries)
        if 'occasion' in request.GET:
            occasions = request.GET.getlist('occasion')
            current_occasions = occasions
            occasion_queries = Q()
            for occasion in occasions:
                occasion_queries |= Q(occasion__icontains=occasion)
            products = products.filter(occasion_queries)

        if 'max_price' in request.GET:
            max_price = request.GET.get('max_price')
            if max_price and max_price.isdigit():
                products = products.filter(price__lte=int(max_price))
    
    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'high_rating':
        products = products.order_by('-rating')
    elif sort_by == 'low_rating':
        products = products.order_by('rating')
    elif sort_by == 'average_rating':
        products = products.order_by('-rating')  # assuming average is high rating
    elif sort_by == 'new_desc':
        products = products.order_by('-id')  # assuming id for newness
    elif sort_by == 'new_asc':
        products = products.order_by('id')
    # else default, no order_by
    
            # Paginate products - 15 per page
    paginator = Paginator(products, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    query_params = request.GET.copy()
    query_params.pop('page', None)
    
    f_queries = Q(tags__icontains='"featured"')
    f_products = Product.objects.filter(f_queries)[:4]

    sale_queries = Q(tags__icontains='"sale"')
    sale_products = Product.objects.filter(sale_queries).order_by('?')[:2]

    context = {
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'current_categories': categories,
        'current_tags': current_tags,
        'current_occasions': current_occasions,
        'query_params': query_params.urlencode(),
        'f_products': f_products,
        'sale_products': sale_products,
    } 

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id).order_by('?')[:8]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)