from django.contrib import admin

from .models import Order, Product, Category, Filial, Report, Vacancy, Warehouse


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
    list_display = ['name', 'address', 'work_week', 'open_at', 'close_at', 'phone']


@admin.register(Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_message']

    def short_message(self, report):
        msg = report.message
        if len(msg) < 25:
            return report.message[:25]
        return f"{report.message[:25]}..."
    
    short_message.short_description = 'Short Message'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['vacancy', 'need_status']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['snack', 'purchased_price', 'sold_price', 'stock']

