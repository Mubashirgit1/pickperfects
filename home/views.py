from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render,redirect
from products.models import Product

# Create your views here.

def index(request):

    all_products = Product.objects.order_by('?')[:8]
    new_products = Product.objects.filter(tags__icontains='new').order_by('?')[:4]
    fetured_products = Product.objects.filter(tags__icontains='featured').order_by('?')[:4]
    top_rated_products = Product.objects.order_by('-rating')[:4]
    sale_products = Product.objects.filter(tags__icontains='sale').order_by('?')[:2]
    context = {
        'all_products': all_products,
        'new_products': new_products,
        'featured_products': fetured_products,
        'top_rated_products': top_rated_products,
        'sale_products': sale_products,
    }
    return render(request, 'home/index.html', context)

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
