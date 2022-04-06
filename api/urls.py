
from django.urls import path

from order.views import OrderListView, OrderCreateView
from order.reports import order_report
from user.views import OperatorListView, OperatorCreateView
from product.views import ProductListView, ProductCreateView

urlpatterns = [
    # Orders
    path('orders/', OrderListView.as_view(), name='orders-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),

    # Operator
    path('operators/', OperatorListView.as_view(), name='operators-list'),
    path('operators/create/', OperatorCreateView.as_view(), name='operator-create'),

    # Products
    path('products/', ProductListView.as_view(), name='products-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),

    # Report
    path('report/', order_report, name='report-list'),
]