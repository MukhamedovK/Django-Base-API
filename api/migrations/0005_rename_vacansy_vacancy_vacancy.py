# Generated by Django 5.0.3 on 2024-04-08 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_order_created_at_order_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='vacansy',
            new_name='vacancy',
        ),
    ]