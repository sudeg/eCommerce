# Generated by Django 3.0.5 on 2020-05-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_designer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='slug',
            field=models.SlugField(default=True, unique=True),
            preserve_default=False,
        ),
    ]