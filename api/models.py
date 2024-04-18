from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserStatus(models.TextChoices):
    USER = "user", "User"
    CHIEF = "chief", "Chief"
    ADMIN = "admin", "Admin"
    DELIVER = "deliver", "Deliver"
    MANAGER = "manager", "Manager"


class OrderStatus(models.TextChoices):
    DELIVERED = "delivered", "Order Delivered"
    ON_ORDER = "on_order", "On Order"
    PAYMENT_SUCCESS = "success", "Payment Success"
    ORDER_CREATED = "created", "Order Created"
    DELIVERING = "delivering", "Delivering"


class User(AbstractUser):
    image = models.ImageField(upload_to='avatar', default='default_img/avatar.png')
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
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


class Category(models.Model):
    image = models.ImageField(upload_to='category' , default='default_img/category.png')
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='products', default='default_img/product.png')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField(default=0)
    sold_qty = models.PositiveIntegerField(default=0)
    recipe = models.ManyToManyField('Warehouse')

    def __str__(self) -> str:
        return self.title


class Filial(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    open_at = models.TimeField(null=True)
    close_at = models.TimeField(null=True)
    work_week = models.CharField(max_length=100, default="Du-Yak")
    phone = models.CharField(max_length=50)
    branch_manager = models.ForeignKey(User, related_name='filial_branch_manager', on_delete=models.CASCADE)
    main_chief = models.ForeignKey(User, related_name="filial_main_chief", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=OrderStatus.choices, default=OrderStatus.ORDER_CREATED
    )
    count = models.PositiveSmallIntegerField(default=1)
    total_price = models.PositiveBigIntegerField()
    order_created = models.DateTimeField(auto_now_add=True)
    on_order = models.DateTimeField(null=True, blank=True)
    delivering = models.DateTimeField(null=True, blank=True)
    order_delivered = models.DateTimeField(null=True, blank=True)
    payment_success = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == OrderStatus.ORDER_CREATED and not self.order_created:
            self.order_created = timezone.now()
        elif self.status == OrderStatus.ON_ORDER and not self.on_order:
            self.on_order = timezone.now()
        elif self.status == OrderStatus.DELIVERING and not self.Delivering:
            self.Delivering = timezone.now()
        elif self.status == OrderStatus.DELIVERED and not self.order_delivered:
            self.order_delivered = timezone.now()
        elif self.status == OrderStatus.PAYMENT_SUCCESS and not self.payment_success:
            self.payment_success = timezone.now()
        super(Order, self).save(*args, **kwargs)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Vacancy(models.Model):
    image = models.ImageField(upload_to='vacancy', default='default_img/vacancy.png')
    name = models.CharField(max_length=200)
    status = models.BooleanField()
    applied = models.PositiveIntegerField()
    rejected = models.PositiveIntegerField()
    favourite = models.BooleanField()


class Warehouse(models.Model):
    image = models.ImageField(upload_to='warehouse', default='default_img/warehouse.png')
    name = models.CharField(max_length=150)
    purchased_price = models.PositiveBigIntegerField()
    sold_price = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.stock}"
