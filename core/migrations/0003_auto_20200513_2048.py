# Generated by Django 3.0.5 on 2020-05-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_designer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='image',
            field=models.ImageField(default=True, null=True, upload_to='product_images'),
        ),
    ]