# Generated by Django 4.2.5 on 2024-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('full_body', models.TextField()),
                ('category', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('post', models.CharField(max_length=300)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.DeleteModel(
            name='CustomerReview',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]