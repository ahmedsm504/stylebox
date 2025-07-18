from django.db import models
from django.contrib.auth.models import User

class Design(models.Model):
    DESIGN_TYPES = [
        ('button', 'Button'),
        ('card', 'Card'),
        ('navbar', 'Navbar'),
        ('header', 'Header'),
        ('form', 'Form'),
        ('input', 'Input'),
        ('loader', 'Loader'),
        ('radio', 'Radio Button'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    design_type = models.CharField(max_length=20, choices=DESIGN_TYPES)
    html_code = models.TextField()
    css_code = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='designs')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.name} - {self.design_type}"
    
    
    def like_count(self):
     return self.designlike_set.count()



# designs/models.py
from django.contrib.auth.models import User
from django.db import models

# models.py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    is_approved = models.BooleanField(default=False)  # ⬅️ جديد

    def __str__(self):
        return f"{self.user.username} Profile"

# models.py
from django.db import models
from django.contrib.auth.models import User

class DesignLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.ForeignKey('Design', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'design')  # يمنع التكرار
