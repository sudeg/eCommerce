# Generated by Django 3.0.5 on 2020-05-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_designer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designer',
            name='slug',
            field=models.SlugField(),
        ),
    ]
