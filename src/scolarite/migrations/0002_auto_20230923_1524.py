# Generated by Django 3.1.6 on 2023-09-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scolarite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualite',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='Scolarite/Actualite/'),
        ),
        migrations.AddField(
            model_name='emploidutemps',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='Scolarite/EmploisDuTemps/'),
        ),
    ]