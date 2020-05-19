# Generated by Django 3.0.5 on 2020-05-19 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_designer_countdesignerpros'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionalPrinter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default=True, null=True, upload_to='product_images')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
