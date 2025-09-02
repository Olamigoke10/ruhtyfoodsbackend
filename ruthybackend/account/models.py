from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # For password reset / OTP verification
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    reset_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name else self.username

    def set_otp(self, otp_code):
        """Set OTP and timestamp"""
        self.otp = otp_code
        self.otp_created_at = timezone.now()
        self.save()

    def verify_otp(self, otp_code, expiry_minutes=10):
        """Check if OTP is valid and not expired"""
        if self.otp != otp_code:
            return False
        if self.otp_created_at and timezone.now() > self.otp_created_at + timedelta(minutes=expiry_minutes):
            return False
        return True
