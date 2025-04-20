from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    """
    View manager
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home') 
        else:
            print(form.errors)  # Debugging: Print form errors to the console
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'mega_motive/index.html', context)

