# Generated by Django 3.1.6 on 2023-09-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_auto_20230922_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
