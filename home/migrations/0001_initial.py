# Generated by Django 4.2.5 on 2024-05-06 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField()),
                ('slug', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(blank=True, max_length=200)),
                ('slug', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('post', models.CharField(max_length=300)),
                ('comment', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500)),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
                ('ulr', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('desription', models.TextField(blank=True)),
                ('specification', models.TextField(blank=True)),
                ('stock', models.CharField(choices=[('in_stock', 'In Stock'), ('out of stock', 'Out of Stock')], max_length=50)),
                ('labels', models.CharField(blank=True, choices=[('', 'default'), ('new', 'new'), ('sale', 'sale'), ('hot', 'hot')], max_length=50)),
                ('slug', models.CharField(default='', max_length=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'ordering': ('id', 'price', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('quantity', models.FloatField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('checkout', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]