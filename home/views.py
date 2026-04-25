from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

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
