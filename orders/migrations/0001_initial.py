# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FullOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.TextField()),
                ('quantity', models.TextField()),
                ('customer_name', models.TextField()),
                ('total_amount', models.DecimalField(max_digits=12, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='FullOrderLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.TextField()),
                ('product_name', models.TextField()),
                ('product_quantity', models.TextField()),
                ('customer_name', models.TextField()),
                ('gross_amount', models.DecimalField(max_digits=12, decimal_places=4)),
                ('total_amount', models.DecimalField(max_digits=12, decimal_places=4)),
            ],
        ),
    ]
