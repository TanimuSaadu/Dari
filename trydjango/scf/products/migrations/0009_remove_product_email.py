# Generated by Django 2.0.7 on 2020-10-05 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201005_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
    ]
