from django.contrib import admin

from .models import User, Order, Product, Category, Filial, Report, Vacancy, Warehouse, Client


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'status']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'count', 'status']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'sold_qty']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'work_time', 'phone']


@admin.register(Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_message']

    def short_message(self, report):
        return f"{report.message[:25]}..."
    short_message.short_description = 'Short Message'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['vacansy', 'need_status']


# @admin.register(Warehouse)
# class WarehouseAdmin(admin.ModelAdmin):
#     list_display = ['']


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['']

