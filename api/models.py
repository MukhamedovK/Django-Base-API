from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    # job = models.CharField(max_length=100)
    # salary = models.PositiveIntegerField()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='auth_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='auth_user_permissions'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} {self.surname}"

