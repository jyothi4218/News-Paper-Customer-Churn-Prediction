from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True)
    reason_for_switch = models.CharField(max_length=255, blank="Not Switching", null=True)


