from queue import Full
from django.contrib import admin
from .models import FullOrder, FullOrderLine
# Register your models here.

admin.site.register(FullOrder,FullOrderLine)