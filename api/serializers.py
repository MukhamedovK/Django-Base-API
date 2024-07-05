from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from datetime import datetime
from environs import Env

from .models import Filial, Category, Product, Order, Report, Vacancy, Warehouse, User

env = Env()
env.read_env()


class UsersAPISerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "groups",
            "first_name",
            "last_name",
            "user_permissions",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
            "username"
        ]

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url
        try:
            redata["last_login"] = datetime.strftime(
                instance.last_login, "%d-%m-%Y %H:%M:%S"
            )
        except:
            redata["last_login"] = datetime.strftime(
                datetime.now(), "%d-%m-%Y %H:%M:%S"
            )

        return redata


class FilialsAPISerializer(ModelSerializer):
    branch_manager = UsersAPISerializer()
    main_chief = UsersAPISerializer()
    class Meta:
        model = Filial
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["open_at"] = redata["open_at"][:5]
        redata["close_at"] = redata["close_at"][:5]

        return redata


class VacancyAPISerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url

        return redata


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url

        return redata


class WarehouseAPISerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"

    def update(self, instance, validated_data):
        if "sold_price" in validated_data:
            sold_price = instance.sold_price
            percent = validated_data["sold_price"]
            percent_price = sold_price * (percent / 100)
            instance.sold_price += percent_price
            instance.save()
        return instance

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url

        return redata


class ProductAPISerializer(ModelSerializer):
    category = CategoriesSerializer()
    recipe = WarehouseAPISerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = env.str('DOMEN') + instance.image.url

        return redata


class ReportsAPISerializer(ModelSerializer):
    user = UsersAPISerializer()

    class Meta:
        model = Report
        fields = "__all__"


class OrdersAPISerializer(ModelSerializer):
    user = UsersAPISerializer()
    product = ProductAPISerializer()
    filial = FilialsAPISerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["order_created"] = datetime.strftime(instance.order_created, "%a, %d %b %Y, %I:%M %p")
        if instance.on_order:
            redata["on_order"] = datetime.strftime(instance.on_order, "%a, %d %b %Y, %I:%M %p")
        if instance.delivering:
            redata["delivering"] = datetime.strftime(instance.delivering, "%a, %d %b %Y, %I:%M %p")
        if instance.order_delivered:
            redata["order_delivered"] = datetime.strftime(instance.order_delivered, "%a, %d %b %Y, %I:%M %p")
        if instance.payment_success:
            redata["payment_success"] = datetime.strftime(instance.payment_success, "%a, %d %b %Y, %I:%M %p")

        return redata
