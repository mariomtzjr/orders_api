
from django.urls import path

from order.views import OrderListView, OrderCreateView
from user.views import (
    OperatorListView,
    OperatorCreateView,
    OperatorDetailView,
    ComensalDetailView,
    )
from product.views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    # Orders
    path('orders/', OrderListView.as_view(), name='orders-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),

    # Operator
    path('operators/', OperatorListView.as_view(), name='operators-list'),
    path('operators/<int:pk>', OperatorDetailView.as_view(), name='operator-detail'),
    path('operators/create/', OperatorCreateView.as_view(), name='operator-create'),

    # Comensales
    path('comensales/<int:pk>', ComensalDetailView.as_view(), name='comensal-detail'),

    # Products
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
]