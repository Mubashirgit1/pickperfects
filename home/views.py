from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render,redirect
from products.models import Product
import random
# Create your views here.

def index(request):
 # Get only needed fields + category (optimization)
    base_qs = Product.objects.select_related('category').only(
        'id', 'name', 'price', 'image', 'sku', 'rating', 'tags', 'category__friendly_name'
    )

    # Convert to list once (avoids multiple DB hits)
    products_list = list(base_qs)

    # Random selection (faster than order_by('?'))
    all_products = random.sample(products_list, min(len(products_list), 20))
    grouped_products = chunk_products(all_products, 4)

    # Filter in Python (since already loaded)
    new_products = [p for p in products_list if 'new' in (p.tags or [])][:4]
    featured_products = [p for p in products_list if 'featured' in (p.tags or [])][:4]
    sale_products = [p for p in products_list if 'sale' in (p.tags or [])][:5]
    
    # Top rated (still better via DB)
    top_rated_products = base_qs.order_by('-rating')[:6]

    context = {
        'all_products': all_products,
        'grouped_products': grouped_products,
        'new_products': new_products,
        'featured_products': featured_products,
        'top_rated_products': top_rated_products,
        'sale_products': sale_products,
    }

    return render(request, 'home/index.html', context)

def chunk_products(products, chunk_size):
    return [products[i:i + chunk_size] for i in range(0, len(products), chunk_size)]

def contact_view(request):
    """Handle the Contact Us form submission and display confirmation messages."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            messages.success(
                request,
                f"Thank you {name}! We’ll get back to you soon.",
                extra_tags='hide_bag',
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('nl_email')
        if email:
            # Here you would typically save the email to your database or send it to your email marketing service
            messages.success(request, "Thank you for signing up for our newsletter!", extra_tags='newsletter')
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect('home')

def custom_404(request, exception):
    return render(request, 'home/404.html', status=404)
