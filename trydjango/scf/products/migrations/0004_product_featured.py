# Generated by Django 2.0.7 on 2020-04-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200421_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]