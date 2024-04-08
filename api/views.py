from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Filial, Category, Product, Vacancy, Warehouse, Order, Report
from .utils import get_template, post_template, put_template, delete_template
from . import serializers


class UsersAPI(APIView):
    serializer = serializers.UsersAPISerializer
    def get(self, request):
        users = get_template(request, User, self.serializer)
        return Response({"users": users}, status=status.HTTP_200_OK)

    def post(self, request):
        password = request.data.get("password")
        if len(password) < 8:
            return Response(
                {"error": "The password must be at least 8 characters long!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        user_id: int = request.data.get("user_id")
        data, HttpStatus = put_template(request, User, self.serializer, user_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        user_id: int = request.data.get("user_id")
        data, HttpStatus = delete_template(request, User, user_id)
        return Response(data, status=HttpStatus)


class CategoryAPI(APIView):
    serializer = serializers.CategoriesSerializer
    def get(self, request):
        data = get_template(request, Category, self.serializer)
        return Response({"categories": data}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        category_id: int = request.data.get("category_id")
        data, HttpStatus = put_template(request, Category, self.serializer, category_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):  
        category_id: int = request.data.get("category_id")
        data, HttpStatus = delete_template(request, Category, category_id)
        return Response(data, status=HttpStatus)


class ProductsAPI(APIView):
    serializer = serializers.ProductAPISerializer
    def get(self, request):
        data = get_template(request, Product, self.serializer)
        return Response({"products": data}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        product_id: int = request.data.get("product_id")
        data, HttpStatus = put_template(request, Product, self.serializer, product_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        product_id: int = request.data.get("product_id")
        data, HttpStatus = delete_template(request, Product, product_id)
        return Response(data, status=HttpStatus)


class FilialsAPI(APIView):
    serializer = serializers.FilialsAPISerializer
    def get(self, request):
        data = get_template(request, Filial, self.serializer)
        return Response({"filials": data}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        filial_id: int = request.data.get("filial_id")
        data, HttpStatus = put_template(request, Filial, self.serializer, filial_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        filial_id: int = request.data.get("filial_id")
        data, HttpStatus = delete_template(request, Filial, filial_id)
        return Response(data, status=HttpStatus)


class VacancyAPI(APIView):
    serializer = serializers.VacancyAPISerializer
    def get(self, request):
        data = get_template(request, Vacancy, self.serializer)
        return Response({"vacancys": data}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        vacancy_id:int = request.data.get('vacancy_id')
        data, HttpStatus = put_template(request, Vacancy, self.serializer, vacancy_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        vacancy_id:int = request.data.get('vacancy_id')
        data, HttpStatus = delete_template(request, Vacancy, vacancy_id)
        return Response(data, status=HttpStatus)
    

class WarehouseAPI(APIView):
    serializer = serializers.WarehouseAPISerializer
    def get(self, request):
        data = get_template(request, Warehouse, self.serializer)
        return Response({"warehouse": data}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        item_id:int = request.data.get('item_id')
        data, HttpStatus = put_template(request, Warehouse, self.serializer, item_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        item_id:int = request.data.get('item_id')
        data, HttpStatus = delete_template(request, Warehouse, item_id)
        return Response(data, status=HttpStatus)
    

class ReportAPI(APIView):
    serializer = serializers.ReportsAPISerializer
    def get(self, request):
        reports = get_template(request, Report, self.serializer)
        return Response({"reports": reports}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        message_id:int = request.data.get('message_id')
        data, HttpStatus = put_template(request, Report, self.serializer, message_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        message_id:int = request.data.get('message_id')
        data, HttpStatus = delete_template(request, Report, message_id)
        return Response(data, status=HttpStatus)


class OrdersAPI(APIView):
    serializer = serializers.OrdersAPISerializer
    def get(self, request):
        orders = get_template(request, Order, self.serializer)
        return Response({"orders": orders}, status=status.HTTP_200_OK)

    def post(self, request):
        data, HttpStatus = post_template(request, self.serializer)
        return Response(data, status=HttpStatus)

    def put(self, request):
        order_id:int = request.data.get('order_id')
        data, HttpStatus = put_template(request, Order, self.serializer, order_id)
        return Response(data, status=HttpStatus)

    def delete(self, request):
        order_id:int = request.data.get('order_id')
        data, HttpStatus = delete_template(request, Order, order_id)
        return Response(data, status=HttpStatus)
