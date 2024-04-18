from django.contrib import admin

from .models import Order, Product, Category, Filial, Report, Vacancy, Warehouse, User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "status", "is_superuser", "is_active"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "product", 'filial', "count", "status"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "discount", "sold_qty"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
        "work_week",
        "open_at",
        "close_at",
        "phone",
        "branch_manager",
        "main_chief",
    ]


@admin.register(Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ["user", "message", "created_at"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["name", "status", 'applied', 'rejected']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["name", "purchased_price", "sold_price", "stock"]
