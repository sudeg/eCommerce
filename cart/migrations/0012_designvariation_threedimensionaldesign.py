# Generated by Django 3.0.5 on 2020-05-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20200505_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ThreeDimensionalDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('imageOne', models.ImageField(null=True, upload_to='product_images')),
                ('imageTwo', models.ImageField(null=True, upload_to='product_images')),
                ('imageThree', models.ImageField(null=True, upload_to='product_images')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('available_colours', models.ManyToManyField(null=True, to='cart.ColourVariation')),
                ('available_sizes', models.ManyToManyField(null=True, to='cart.SizeVariation')),
                ('relatedType', models.ManyToManyField(null=True, to='cart.DesignVariation')),
            ],
        ),
    ]
