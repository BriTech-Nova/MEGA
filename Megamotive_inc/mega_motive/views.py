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