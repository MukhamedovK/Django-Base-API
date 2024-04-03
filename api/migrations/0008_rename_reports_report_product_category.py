# Generated by Django 5.0.3 on 2024-04-03 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_category_client_filial_product_vacancy_warehouse_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reports',
            new_name='Report',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
