# Generated by Django 2.0.7 on 2020-10-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200421_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
