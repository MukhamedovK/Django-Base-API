from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user_api, name='loginAPI'),
    path('registration/', views.create_user_api, name='create-user'),

    path('users/', views.users_api, name='userAPI'),
    path('users/<int:user_id>/', views.users_api, name='one-user'),
    path('users/edit/<int:user_id>/', views.update_user_api, name='user-edit'),
    path('users/delete/<int:user_id>/', views.delete_user_api, name='user-delete'),

    path('categories/', views.categories_api, name='categoryAPI'),
    path('categories/<int:category_id>/', views.categories_api, name='one-category'),
    path('categories/create/', views.create_category_api, name='create-category'),
    path('categories/edit/<int:category_id>/', views.update_category_api, name='category-edit'),
    path('categories/delete/<int:category_id>/', views.delete_category_api, name='category-delete'),

    path('products/', views.products_api, name='productAPI'),
    path('products/<int:product_id>/', views.products_api, name='one-product'),
    path('products/create/', views.create_product_api, name='create-product'),
    path('products/edit/<int:product_id>/', views.update_product_api, name='product-edit'),
    path('products/delete/<int:product_id>/', views.delete_product_api, name='product-delete'),

    path('filials/', views.filials_api, name='filialAPI'),
    path('filials/<int:filial_id>/', views.filials_api, name='one-filial'),
    path('filials/create/', views.create_filial_api, name='create-filial'),
    path('filials/edit/<int:filial_id>/', views.update_filial_api, name='filial-edit'),
    path('filials/delete/<int:filial_id>/', views.delete_filial_api, name='filial-delete'),

    path('vacancys/', views.vacancys_api, name='vacancyAPI'),
    path('vacancys/<int:vacancy_id>/', views.vacancys_api, name='one-vacancy'),
    path('vacancys/create/', views.create_vacancy_api, name='create-vacancy'),
    path('vacancys/edit/<int:vacancy_id>/', views.update_vacancy_api, name='vacancy-edit'),
    path('vacancys/delete/<int:vacancy_id>/', views.delete_vacancy_api, name='vacancy-delete'),

    path('warehouse/', views.warehouse_api, name='warehouseAPI'),
    path('warehouse/<int:item_id>/', views.warehouse_api, name='one-warehouse'),
    path('warehouse/create/', views.create_item_api, name='create-warehouse'),
    path('warehouse/edit/<int:item_id>/', views.update_item_api, name='warehouse-edit'),
    path('warehouse/delete/<int:item_id>/', views.delete_item_api, name='warehouse-delete'),

    path('reports/', views.reports_api, name='reportAPI'),
    path('reports/<int:report_id>/', views.reports_api, name='one-report'),
    path('reports/create/', views.create_report_api, name='create-report'),
    path('reports/edit/<int:report_id>/', views.update_report_api, name='report-edit'),
    path('reports/delete/<int:report_id>/', views.delete_report_api, name='report-delete'),
    
    path('orders/', views.orders_api, name='orderAPI'),
    path('orders/<int:order_id>/', views.orders_api, name='one-order'),
    path('orders/create/', views.create_item_api, name='create-order'),
    path('orders/edit/<int:order_id>/', views.update_item_api, name='order-edit'),
    path('orders/delete/<int:order_id>/', views.delete_item_api, name='order-delete'),
]