# Generated by Django 3.1.6 on 2023-09-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formation',
            options={'verbose_name': 'Formation'},
        ),
        migrations.AlterField(
            model_name='formation',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='slug',
            field=models.SlugField(blank=True, default='Acune valeur', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
