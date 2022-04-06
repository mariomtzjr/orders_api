from user.models import Comensal, Operator
from product.models import Product


def parse_orders(queryset):
    order_data = {}
    product_data = {}
    orders = []
    products = []
        
    for order in queryset:
        comensal = Comensal.objects.get(pk=order.comensal.id)
        operator = Operator.objects.get(pk=order.operador.id)

        for order_item in order.order_items.all():
            product = Product.objects.get(pk=order_item.product.id)
            product_data["id"] = product.id
            product_data["name"] = product.__str__()
            product_data["quantity"] = order_item.qty
            product_data["unit_price"] = order_item.unit_price
            product_data["total"] = order_item.total_price
            products.append(product_data)
            product_data = {}
        products = []

        order_data = {
            'order_items': products,
        }
        order_data["id"] = order.id
        order_data["operador"] = {"id": operator.employee_number, "name": operator.__str__()}
        order_data["comensal"] = {"id": comensal.id, "name": comensal.__str__()}
        order_data["grand_total"] = order.grand_total
        order_data["date"] = order.date
            
        orders.append(order_data)
    
    return orders