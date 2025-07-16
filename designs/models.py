from django.db import models
from django.contrib.auth.models import User

class Design(models.Model):
    DESIGN_TYPES = [
        ('button', 'Button'),
        ('card', 'Card'),
        ('navbar', 'Navbar'),
        ('header', 'Header'),
        ('form', 'Form'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    design_type = models.CharField(max_length=20, choices=DESIGN_TYPES)
    html_code = models.TextField()
    css_code = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='designs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.design_type}"

# designs/models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
