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
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "date_joined",
            "is_superuser",
        ]

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = f"http://{env.str('DOMEN')}{instance.image.url}"
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
        redata["image"] = f"http://{env.str('DOMEN')}{instance.image.url}"

        return redata


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = f"http://{env.str('DOMEN')}{instance.image.url}"

        return redata


class ProductAPISerializer(ModelSerializer):
    category = CategoriesSerializer()

    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["image"] = f"http://{env.str('DOMEN')}{instance.image.url}"

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
        redata["image"] = f"http://{env.str('DOMEN')}{instance.image.url}"

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
        time_format = datetime.strftime(instance.created_at, "%a, %d %b %Y, %I:%M %p")
        redata["order_created"] = time_format
        redata["on_order"] = time_format
        redata["delivering"] = time_format
        redata["order_delivered"] = time_format
        redata["payment_success"] = time_format

        return redata
