# Generated by Django 3.0.5 on 2020-05-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_printerowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='email',
            field=models.CharField(default=True, max_length=150, null=True),
        ),
    ]