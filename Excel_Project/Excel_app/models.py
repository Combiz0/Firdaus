from datetime import timezone
from django.db import models
from django.utils import timezone
# Create your models here.

class EmailAccess(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date  = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email
