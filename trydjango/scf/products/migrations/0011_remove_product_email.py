# Generated by Django 2.0.7 on 2020-10-05 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
    ]