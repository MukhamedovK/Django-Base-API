from django.db import models
from django.contrib.auth.models import AbstractUser


class UserStatus(models.TextChoices):
    USER = "user", "User"
    CHEF = "chef", "Chef"
    ADMIN = "admin", "Admin"


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.EmailField(null=True)
    status = models.CharField(
        max_length=100, choices=UserStatus.choices, default=UserStatus.USER
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username.lower()
        if not self.name:
            self.name = self.username.title()
        super().save(*args, **kwargs)

