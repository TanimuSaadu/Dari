# Generated by Django 2.0.7 on 2020-10-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201005_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]