# Generated by Django 5.0.3 on 2024-04-18 01:16

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/static/default_img/category.png', upload_to='category')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/static/default_img/vacancy.png', upload_to='vacancy')),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('applied', models.PositiveIntegerField()),
                ('rejected', models.PositiveIntegerField()),
                ('favourite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/static/default_img/warehouse.png', upload_to='warehouse')),
                ('name', models.CharField(max_length=150)),
                ('purchased_price', models.PositiveBigIntegerField()),
                ('sold_price', models.PositiveBigIntegerField()),
                ('stock', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(default='/static/default_img/avatar.png', upload_to='avatar')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('status', models.CharField(choices=[('user', 'User'), ('chief', 'Chief'), ('admin', 'Admin'), ('deliver', 'Deliver'), ('manager', 'Manager')], default='user', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('open_at', models.TimeField(null=True)),
                ('close_at', models.TimeField(null=True)),
                ('work_week', models.CharField(default='Du-Yak', max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('branch_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filial_branch_manager', to=settings.AUTH_USER_MODEL)),
                ('main_chief', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filial_main_chief', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/static/default_img/product.png', upload_to='products')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('discount', models.FloatField(default=0)),
                ('sold_qty', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('recipe', models.ManyToManyField(to='api.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('delivered', 'Order Delivered'), ('on_order', 'On Order'), ('success', 'Payment Success'), ('created', 'Order Created'), ('delivering', 'Delivering')], default='created', max_length=100)),
                ('count', models.PositiveSmallIntegerField(default=1)),
                ('total_price', models.PositiveBigIntegerField()),
                ('order_created', models.DateTimeField(auto_now_add=True)),
                ('on_order', models.DateTimeField(blank=True, null=True)),
                ('delivering', models.DateTimeField(blank=True, null=True)),
                ('order_delivered', models.DateTimeField(blank=True, null=True)),
                ('payment_success', models.DateTimeField(blank=True, null=True)),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.filial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
