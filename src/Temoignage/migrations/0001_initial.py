# Generated by Django 3.1.6 on 2023-09-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, unique=True, verbose_name="Nom & prenom de l'étudiant ")),
                ('content', models.TextField(max_length=255, verbose_name='Commentaire')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Temoignage/Image/')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
            ],
            options={
                'verbose_name': 'Temoignage',
                'ordering': ['-fullname'],
            },
        ),
    ]
