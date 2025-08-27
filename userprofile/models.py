from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/',null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(null=True, blank=True)
    link_1 = models.CharField(null=True, blank=True)
    link_2 = models.CharField(null=True, blank=True)
    link_3 = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.user.username