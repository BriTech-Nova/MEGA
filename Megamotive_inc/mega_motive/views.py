from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, 'mega_motive/index.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')  # Replace 'index' with the name of your homepage URL
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'mega_motive/index.html', {'form': form})