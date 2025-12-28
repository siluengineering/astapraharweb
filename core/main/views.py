from django.shortcuts import render, redirect
from .forms import ContactForm, MembershipForm
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact1(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # Handle form logic (e.g., send email)
        return redirect('home')
    return render(request, 'main/contact.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, you would send an email here
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        # This handles the initial GET request
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def membership1(request):
    form = MembershipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/membership.html', {'form': form})

def membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            # This saves the data to the Membership model in your database
            form.save() 
            messages.success(request, 'Welcome to the community! Your membership has been registered.')
            return redirect('home')
    else:
        form = MembershipForm()
    
    return render(request, 'main/membership.html', {'form': form})