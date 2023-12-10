# Generated by Django 4.2.4 on 2023-09-03 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_colors_options_alter_size_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount_product',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_product', to='core.colors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount_product',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_product', to='core.size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_product', to='core.colors'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_product', to='core.size'),
        ),
    ]
