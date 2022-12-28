# Generated by Django 4.1 on 2022-12-28 07:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.IntegerField()),
                ('protein', models.FloatField()),
                ('total_fat', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('trans_fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('sugars', models.FloatField()),
                ('sodium', models.FloatField()),
                ('cholesterol', models.FloatField(blank=True, null=True)),
                ('vitaminB2', models.FloatField(blank=True, null=True)),
                ('vitaminB3', models.FloatField(blank=True, null=True)),
                ('vitaminB6', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('supermarket', models.CharField(choices=[('Wellcome', 'Wellcome'), ('Parknshop', 'Parknshop'), ('Jasons', 'Jasons'), ('Aeon', 'Aeon'), ('Dchfood', 'Dchfood'), ('Watsons', 'Watsons'), ('Mannings', 'Mannings'), ('Ztore', 'Ztore')], default='1Wellcome', max_length=10)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='FoodProducts',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('barcode', models.CharField(blank=True, max_length=300)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('manufacturer', models.CharField(blank=True, max_length=200)),
                ('brand', models.CharField(blank=True, max_length=200)),
                ('nutrition', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='food_products.nutritioninformation')),
                ('product_price', models.ManyToManyField(blank=True, to='food_products.productprice')),
            ],
        ),
    ]
