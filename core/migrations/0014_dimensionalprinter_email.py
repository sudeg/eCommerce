# Generated by Django 3.0.5 on 2020-05-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_dimensionalprinter'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimensionalprinter',
            name='email',
            field=models.EmailField(default=True, max_length=150, null=True),
        ),
    ]
