from django.shortcuts import render

from inlägg.models import GuestbookEntry

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'About.html')

def guestbook(request):
    entries = GuestbookEntry.objects.all().order_by('-created_at')

    return render(request, 'guestbook.html', {'entries': entries})