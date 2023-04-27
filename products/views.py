import json
# from urllib import response
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db.models import Q


@csrf_exempt
def create_product(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            product = Product()
            product.product_code = body.get('product_code')
            product.product_name = body.get('product_name')
            product.unit_price = body.get('unit_price')
            product.tax_percent = body.get('tax_percent')
            product.save()
            cust_id = product.id
            response = {
                'status': True,
                'code': 200,
                'message': 'Product Saved with ID:{cust_id}'.format(cust_id=cust_id)
            }

    except IntegrityError as e: 
        response = {
            'status': False,
            'code': 500,
            'message': 'Product code is not unique'
        }
        
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)

@csrf_exempt
def get_all_product(request):
    response = {}
    try:
        if request.method == "POST":
            response = list(Product.objects.order_by("id").values())
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def get_prod_by_code(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('product_code')
            product_filter_q = Q(product_code=code)
            response = Product.objects.values().filter(product_filter_q).first()
    except Product.DoesNotExist:
        response = {
            'status': False,
            'code':500,
            'message': 'Product code does not exist'
        }
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def update_product(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('product_code')
            product_filter_q = Q(product_code=code)
            product = Product.objects.filter(product_filter_q).first()
            product.product_code = body.get('product_code')
            product.product_name = body.get('product_name')
            product.unit_price = body.get('unit_price')
            product.tax_percent = body.get('tax_percent')
            product.save()
            cust_id = product.id
            response = {
                'status': True,
                'code': 200,
                'message': 'Product updated with ID:{cust_id}'.format(cust_id=cust_id)
            }
    except Product.DoesNotExist:
        response = {
            'status': False,
            'code': 500,
            'message': 'Product code does not exist'
        }      
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response,safe=False)


@csrf_exempt
def delete_product(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('product_code')
            product_filter_q = Q(product_code=code)
            product = Product.objects.filter(product_filter_q).first()
            prod_id = product.id
            product.delete()
            response = {
                'status': True,
                'code': 200,
                'message': 'Product deleted with ID:{prod_id}'.format(prod_id=prod_id)
            }
    except Product.DoesNotExist:
        response = {
            'status': False,
            'code':500,
            'message': 'Product code does not exist'
        }
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response,safe=False)
    
def products_home(request):
    return render(request,'products/product.html')