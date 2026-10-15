from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'About.html')

def guestbook(request):
    return render(request, 'guestbook.html')