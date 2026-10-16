from django.shortcuts import redirect, render

from inlägg.models import GuestbookEntry

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'About.html')

def guestbook(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        email = request.POST.get('email')

        
        entry = GuestbookEntry(name=name, content=content, email=email)
        entry.save()

        return redirect('guestbook')

    entries = GuestbookEntry.objects.all().order_by('-created_at')



    return render(request, 'guestbook.html', {'entries': entries})