from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('DISTRIBUTOR', 'Distributor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='DISTRIBUTOR')

    def __str__(self):
        return f"{self.username} ({self.role})"
    

class OTPRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return self.created_at >= timezone.now() - datetime.timedelta(minutes=10)
    