from django.db import models

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    