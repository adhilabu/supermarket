from . import views
from django.conf.urls import url

app_name="products"

urlpatterns = [
    url(r'^$', views.products_home),
    url(r'^create/$', views.create_product),
    url(r'^getall/$', views.get_all_product),
    url(r'^getbycode/$', views.get_prod_by_code),
    url(r'^update/$', views.update_product),
    url(r'^delete/$', views.delete_product)
]
