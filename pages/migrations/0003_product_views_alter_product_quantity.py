# Generated by Django 4.2 on 2023-04-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество продукта'),
        ),
    ]
