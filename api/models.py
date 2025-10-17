from django.db import models


class UserProfile(models.Model):
    """
    Model to store user profile information.
    """
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    stack = models.CharField(max_length=100, default='Python/Django')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
