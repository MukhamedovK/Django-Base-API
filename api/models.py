from django.db import models
from accounts.models import User


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    DELIVERING = "delivering", "Delivering"
    SUCCESS = "success", "Success"


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField(default=0)
    sold_qty = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Filial(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    work_week = models.CharField(max_length=100, default="Du-Yak")
    phone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    count = models.PositiveSmallIntegerField(default=1)
    total_price = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()


class Vacancy(models.Model):
    vacancy = models.CharField(max_length=200)
    need_status = models.BooleanField()


class Warehouse(models.Model):
    snack = models.CharField(max_length=150)
    purchased_price = models.PositiveBigIntegerField()
    sold_price = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()



