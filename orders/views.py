from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import FullOrderLine,FullOrder
# Create your views here.

def order_home(request):
    return render(request,'orders/order.html')

@csrf_exempt
def create_order(request):
    response = {}
    try:
        if request.method == "POST":
            print(request.method)
            orders = json.loads(request.body)
            fullOrderLine = FullOrderLine()
            fullOrder = FullOrder()
            full_order_quantity = 0
            full_order_total = 0
            for order in orders:
                order_id = order.order_id
                order_quantity = order.product_quantity
                order_total = order.total_amount
                customer_name = order.customer_name
                fullOrderLine.order_id = order_id
                fullOrderLine.product_name = order.product_name
                fullOrderLine.product_quantity = order_quantity
                fullOrderLine.customer_name = customer_name
                fullOrderLine.gross_amount = order.gross_amount
                fullOrderLine.total_amount = order_total
                fullOrderLine.save()
                full_order_quantity += order_quantity
                full_order_total += order_total
            fullOrder.order_id = order_id
            fullOrder.quantity = full_order_quantity
            fullOrder.customer_name = customer_name
            fullOrder.total_amount = full_order_total
            response = {
                'status': True,
                'code': 200,
                'message': 'Order saved with ID:{order_id}'.format(order_id=order_id)
            }
        
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)