from customers import views
from . import views
from django.conf.urls import url


app_name="orders"


urlpatterns = [
    url(r'^$',views.order_home),
]
