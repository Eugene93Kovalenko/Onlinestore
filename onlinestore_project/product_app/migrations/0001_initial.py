# Generated by Django 4.2.3 on 2023-09-01 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='category/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('color_choices', models.CharField(blank=True, choices=[('Black', 'Black'), ('Red', 'Red'), ('White', 'White'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Green', 'Green')], max_length=10)),
                ('description', models.TextField()),
                ('information', models.TextField()),
                ('slug', models.SlugField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('num_visits', models.IntegerField(default=0)),
                ('collection', models.CharField(blank=True, choices=[('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn')], max_length=10)),
                ('barcode_number', models.IntegerField()),
                ('category', models.ManyToManyField(related_name='products', to='product_app.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='product_app.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product_app.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='product_app.size')),
            ],
            options={
                'verbose_name': 'Товар - Размер - Цвет',
                'verbose_name_plural': 'Товар - Размер - Цвет',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d/')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product_app.product')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]
