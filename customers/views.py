import json
# from urllib import response
from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.db.models import Q


@csrf_exempt
def create_customer(request):
    response = {}
    print(request.method)
    try:
        if request.method == "POST":
            print(request.method)
            body = json.loads(request.body)
            customer = Customer()
            customer.customer_code = body.get('customer_code')
            customer.customer_name = body.get('customer_name')
            customer.customer_address = body.get('customer_address')
            customer.save()
            cust_id = customer.id
            response = {
                'status': True,
                'code': 200,
                'message': 'Customer saved with ID:{cust_id}'.format(cust_id=cust_id)
            }
    except IntegrityError as e: 
        response = {
            'status': False,
            'code': 500,
            'message': 'Customer code is not unique'
        }
        
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def get_all_customer(request):
    response = {}
    try:
        if request.method == "POST":
            response = list(Customer.objects.order_by("id").values())
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def get_cust_by_code(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('customer_code')
            customer_filter_q = Q(customer_code=code)
            response = Customer.objects.values().filter(customer_filter_q).first()
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response, safe=False)


@csrf_exempt
def update_customer(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('customer_code')
            customer_filter_q = Q(customer_code=code)
            customer = Customer.objects.filter(customer_filter_q).first()
            customer.customer_code = body.get('customer_code')
            customer.customer_name = body.get('customer_name')
            customer.customer_address = body.get('customer_address')
            customer.save()
            cust_id = customer.id
            response = {
                'status': True,
                'code': 200,
                'message': 'Customer updated with ID:{cust_id}'.format(cust_id=cust_id)
            }
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response,safe=False)

@csrf_exempt
def delete_customer(request):
    response = {}
    try:
        if request.method == "POST":
            body = json.loads(request.body)
            code = body.get('customer_code')
            customer_filter_q = Q(customer_code=code)
            customer = Customer.objects.filter(customer_filter_q).first()
            cust_id = customer.id
            customer.delete()
            response = {
                'status': True,
                'code': 200,
                'message': 'Customer deleted with ID:{cust_id}'.format(cust_id=cust_id)
            }
    except Exception as e:
        response = {
            'status': False,
            'code': 500,
            'message': 'Internal Server Error'
        }
    return JsonResponse(response,safe=False)


@csrf_exempt
def customers_home(request):
    return render(request,'customers/customer.html')