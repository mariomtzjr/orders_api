# Generated by Django 3.2.12 on 2022-04-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_price_orderitem_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
