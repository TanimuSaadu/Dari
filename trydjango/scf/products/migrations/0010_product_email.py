# Generated by Django 2.0.7 on 2020-10-05 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_product_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=True, max_length=254),
            preserve_default=False,
        ),
    ]
