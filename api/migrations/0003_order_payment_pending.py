# Generated by Django 5.0.3 on 2024-04-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_category_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_pending',
            field=models.BooleanField(default=False),
        ),
    ]
