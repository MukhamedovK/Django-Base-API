from rest_framework.serializers import ModelSerializer, IntegerField
from datetime import datetime

from .models import User, Filial, Category, Product, Order, Report, Vacancy, Warehouse


class UsersAPISerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
            "date_joined",
            "is_superuser",
        ]

    def to_representation(self, instance):
        redata = super().to_representation(instance)
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


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductAPISerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["price"] = f"{redata['price']}$"
        try:
            # redata['discount'] = f"{redata['discount']}%"
            # redata['sold_qty'] = f"{redata['sold_qty']}pcs"
            redata["category"] = instance.category.name
        except:
            redata["category"] = instance["category"].name

        if len(redata["description"]) > 75:
            redata["description"] = f"{redata['description'][:75]}..."

        return redata


class WarehouseAPISerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"

    def update(self, instance, validated_data):
        if "sold_price" in validated_data:
            sold_price = instance.sold_price
            percent = validated_data['sold_price']
            percent_price = sold_price * (percent / 100)
            instance.sold_price += percent_price
            instance.save()
        return instance


class ReportsAPISerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        try:
            redata["user"] = instance.user.username
        except:
            redata["user"] = instance["user"].username

        if len(redata["message"]) > 75:
            redata["message"] = f"{redata['message'][:60]}..."

        return redata


class OrdersAPISerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata["created_at"] = datetime.strftime(
            instance.created_at, "%a, %d %b %Y, %I:%M %p"
        )
        redata["updated_at"] = datetime.strftime(
            instance.updated_at, "%a, %d %b %Y, %I:%M %p"
        )
        try:
            redata["user"] = instance.user.username
            redata["product"] = instance.product.title
            redata["filial"] = instance.filial.name
        except:
            redata["user"] = instance["user"].username
            redata["product"] = instance["product"].title
            redata["filial"] = instance["filial"].name

        return redata
