# Generated by Django 5.0.3 on 2024-04-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sold_qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
