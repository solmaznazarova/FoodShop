# Generated by Django 4.2.4 on 2023-11-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_subscriber_alter_sidebanner_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]