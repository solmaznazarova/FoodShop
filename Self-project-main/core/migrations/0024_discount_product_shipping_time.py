# Generated by Django 4.2.4 on 2023-09-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount_product',
            name='shipping_time',
            field=models.IntegerField(default=1),
        ),
    ]
