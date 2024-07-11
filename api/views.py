from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from environs import Env

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import User, Filial, Category, Product, Vacancy, Warehouse, Order, Report
from .utils import (
    get_template,
    get_one_template,
    post_template,
    put_template,
    delete_template,
    registration_check,
    login_check,
)
from . import serializers


env = Env()
env.read_env()


# LOGIN
class LoginView(APIView):
    @swagger_auto_schema(request_body=serializers.UsersAPISerializer)
    def post(self, request):
        error = login_check(request.data)
        if error:
            return Response({"error": error}, status=status.HTTP_401_UNAUTHORIZED)

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            serializer = serializers.UsersAPISerializer(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "data": serializer.data,
                }
            )
        else:
            return Response(
                {"error": "Authentication failed"}, status=status.HTTP_401_UNAUTHORIZED
            )

# USERS API
@api_view(["GET"])
def users_api(request, user_id=None):
    serializer = serializers.UsersAPISerializer
    if user_id is not None:
        user = get_one_template(request, User, serializer, user_id)
        return Response({"user": user}, status=status.HTTP_200_OK)
    else:
        users = get_template(request, User, serializer)
        return Response({"users": users}, status=status.HTTP_200_OK)


@swagger_auto_schema(request_body=serializers.UsersAPISerializer, method="POST")
@api_view(["POST"])
def create_user_api(request):
    error = registration_check(formData=request.data)
    if error is None:
        data, HttpStatus = post_template(request, serializers.UsersAPISerializer)
        return Response(data, status=HttpStatus)
    return Response(error)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_api(request, user_id):
    data, HttpStatus = put_template(
        request, User, serializers.UsersAPISerializer, user_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user_api(request, user_id):
    data, HttpStatus = delete_template(request, User, user_id)
    return Response(data, status=HttpStatus)


# CATEGORIES API
@api_view(["GET"])
def categories_api(request, category_id=None):
    serializer = serializers.CategoriesSerializer
    if category_id is not None:
        category = get_one_template(request, Category, serializer, category_id)
        return Response({"category": category}, status=status.HTTP_200_OK)
    else:
        categories = get_template(request, Category, serializer)
        return Response({"categories": categories}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_category_api(request):
    data, HttpStatus = post_template(request, serializers.CategoriesSerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_category_api(request, category_id):
    data, HttpStatus = put_template(
        request, Category, serializers.CategoriesSerializer, category_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_category_api(request, category_id):
    data, HttpStatus = delete_template(request, Category, category_id)
    return Response(data, status=HttpStatus)


# PRODUCTS API
@api_view(["GET"])
def products_api(request, product_id=None):
    serializer = serializers.ProductAPISerializer
    if product_id is not None:
        product = get_one_template(request, Product, serializer, product_id)
        return Response({"product": product}, status=status.HTTP_200_OK)
    else:
        products = get_template(request, Product, serializer)
        return Response({"products": products}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_product_api(request):
    data, HttpStatus = post_template(request, serializers.ProductAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_product_api(request, product_id):
    data, HttpStatus = put_template(
        request, Product, serializers.ProductAPISerializer, product_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_product_api(request, product_id):
    data, HttpStatus = delete_template(request, Product, product_id)
    return Response(data, status=HttpStatus)


# FILIALS API
@api_view(["GET"])
def filials_api(request, filial_id=None):
    serializer = serializers.FilialsAPISerializer
    if filial_id is not None:
        filial = get_one_template(request, Filial, serializer, filial_id)
        return Response({"filial": filial}, status=status.HTTP_200_OK)
    else:
        filials = get_template(request, Filial, serializer)
        return Response({"filials": filials}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_filial_api(request):
    data, HttpStatus = post_template(request, serializers.FilialsAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_filial_api(request, filial_id):
    data, HttpStatus = put_template(
        request, Filial, serializers.FilialsAPISerializer, filial_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_filial_api(request, filial_id):
    data, HttpStatus = delete_template(request, Filial, filial_id)
    return Response(data, status=HttpStatus)


# VACANCYS API
@api_view(["GET"])
def vacancys_api(request, vacancy_id=None):
    serializer = serializers.VacancyAPISerializer
    if vacancy_id is not None:
        vacancy = get_one_template(request, Vacancy, serializer, vacancy_id)
        return Response({"vacancy": vacancy}, status=status.HTTP_200_OK)
    else:
        vacancys = get_template(request, Vacancy, serializer)
        return Response({"vacancys": vacancys}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_vacancy_api(request):
    data, HttpStatus = post_template(request, serializers.VacancyAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_vacancy_api(request, vacancy_id):
    data, HttpStatus = put_template(
        request, Vacancy, serializers.VacancyAPISerializer, vacancy_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_vacancy_api(request, vacancy_id):
    data, HttpStatus = delete_template(request, Vacancy, vacancy_id)
    return Response(data, status=HttpStatus)


# WAREHOUSE API
@api_view(["GET"])
def warehouse_api(request, item_id=None):
    serializer = serializers.WarehouseAPISerializer
    if item_id is not None:
        item = get_one_template(request, Warehouse, serializer, item_id)
        return Response({"item": item}, status=status.HTTP_200_OK)
    else:
        items = get_template(request, Warehouse, serializer)
        return Response({"items": items}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_item_api(request):
    data, HttpStatus = post_template(request, serializers.WarehouseAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_item_api(request, item_id):
    data, HttpStatus = put_template(
        request, Warehouse, serializers.WarehouseAPISerializer, item_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_item_api(request, item_id):
    data, HttpStatus = delete_template(request, Warehouse, item_id)
    return Response(data, status=HttpStatus)


# REPORTS API
@api_view(["GET"])
def reports_api(request, report_id=None):
    serializer = serializers.ReportsAPISerializer
    if report_id is not None:
        report = get_one_template(request, Report, serializer, report_id)
        return Response({"report": report}, status=status.HTTP_200_OK)
    else:
        reports = get_template(request, Report, serializer)
        return Response({"reports": reports}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_report_api(request):
    data, HttpStatus = post_template(request, serializers.ReportAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_report_api(request, message_id):
    data, HttpStatus = put_template(
        request, Report, serializers.ReportAPISerializer, message_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_report_api(request, message_id):
    data, HttpStatus = delete_template(request, Report, message_id)
    return Response(data, status=HttpStatus)


# ORDERS API
@api_view(["GET"])
def orders_api(request, order_id=None):
    serializer = serializers.OrdersAPISerializer
    if order_id is not None:
        order = get_one_template(request, Order, serializer, order_id)
        return Response({"order": order}, status=status.HTTP_200_OK)
    else:
        orders = get_template(request, Order, serializer)
        return Response({"orders": orders}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order_api(request):
    data, HttpStatus = post_template(request, serializers.OrdersAPISerializer)
    return Response(data, status=HttpStatus)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order_api(request, order_id):
    data, HttpStatus = put_template(
        request, Order, serializers.OrdersAPISerializer, order_id
    )
    return Response(data, status=HttpStatus)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_order_api(request, order_id):
    data, HttpStatus = delete_template(request, Order, order_id)
    return Response(data, status=HttpStatus)
