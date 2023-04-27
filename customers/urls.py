from turtle import update
from django.conf.urls import url
from . import views

app_name='customers'

urlpatterns = [
    url(r'^$', views.customers_home),
    url(r'^create/$', views.create_customer, name="create"),
    url(r'^getall/$', views.get_all_customer),
    url(r'^getbycode/$', views.get_cust_by_code),
    url(r'^update/$', views.update_customer),
    url(r'^delete/$', views.delete_customer)
]