# Generated by Django 3.1.6 on 2023-09-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_auto_20230923_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='partenaire',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='Presentation/Partenaire/Image/'),
        ),
    ]
