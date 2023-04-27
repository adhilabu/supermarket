# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.TextField(unique=True)),
                ('product_name', models.TextField()),
                ('unit_price', models.DecimalField(max_digits=12, decimal_places=2)),
                ('tax_percent', models.DecimalField(max_digits=12, decimal_places=5)),
            ],
        ),
    ]
