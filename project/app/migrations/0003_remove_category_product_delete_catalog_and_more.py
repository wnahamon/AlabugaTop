# Generated by Django 5.1.4 on 2024-12-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(to='app.product', verbose_name='Product'),
        ),
    ]
