from django.urls import path
from . import views


urlpatterns = [

    # ==========================
    # Dashboard
    # ==========================
    path('', views.dashboard, name='dashboard'),

    # ==========================
    # Customer URLs
    # ==========================
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),

    # ==========================
    # Measurement URLs
    # ==========================
    path("add-measurement/", views.add_measurement, name="add_measurement"),
    path("add-measurement/<int:customer_id>/", views.add_measurement, name="add_measurement_customer"),

    # ==========================
    # Order URLs
    # ==========================
    path('orders/add/', views.add_order, name='add_order'),
    path('orders/update/<int:pk>/', views.update_order, name='update_order'),

    # ==========================
    # Excel Export
    # ==========================
    path('export/customers/', views.export_customers_excel, name='export_customers_excel'),
    path('export/orders/', views.export_orders_excel, name='export_orders_excel'),
]
