from django.db import models
from django.contrib.auth.models import AbstractUser


class UserStatus(models.TextChoices):
    USER = "user", "User"
    CHEF = "chef", "Chef"
    ADMIN = "admin", "Admin"


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    DELIVERING = "delivering", "Delivering"
    SUCCESS = "success", "Success"


class User(AbstractUser):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.EmailField()
    status = models.CharField(
        max_length=100, choices=UserStatus.choices, default=UserStatus.USER
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField(blank=True, null=True, default=0)
    sold_qty = models.PositiveIntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    count = models.PositiveSmallIntegerField(default=0)


class Filial(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    work_time = models.CharField(max_length=100)
    work_week = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Vacancy(models.Model):
    vacansy = models.CharField(max_length=200)
    need_status = models.BooleanField()


class Warehouse(models.Model):
    pass


class Client(models.Model):
    pass
