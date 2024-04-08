from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UsersAPI.as_view(), name='userAPI'),
    path('categories/', views.CategoryAPI.as_view(), name='categoryAPI'),
    path('products/', views.ProductsAPI.as_view(), name='productAPI'),
    path('filials/', views.FilialsAPI.as_view(), name='filialAPI'),
    path('vacancys/', views.VacancyAPI.as_view(), name='vacansyAPI'),
    path('warehouse/', views.WarehouseAPI.as_view(), name='warehouseAPI'),
    path('reports/', views.ReportAPI.as_view(), name='reportAPI'),
    path('orders/', views.OrdersAPI.as_view(), name='orderAPI'),
]