# Generated by Django 4.2.4 on 2023-09-03 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_colors_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colors',
            options={'verbose_name': 'Color', 'verbose_name_plural': 'Colors'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Size', 'verbose_name_plural': 'Size'},
        ),
    ]
