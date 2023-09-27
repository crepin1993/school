# Generated by Django 3.1.6 on 2023-09-23 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created_on', models.DateField(blank=True, null=True, verbose_name='Date de création')),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
            ],
            options={
                'verbose_name': 'Autre actualité',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255, unique=True, verbose_name='Libellé de la classe')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
            ],
            options={
                'verbose_name': 'Classe',
                'ordering': ['-libelle'],
            },
        ),
        migrations.CreateModel(
            name='EmploiDuTemps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created_on', models.DateField(blank=True, null=True, verbose_name='Date de création')),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scolarite.classe')),
            ],
            options={
                'verbose_name': 'Emploie du temps',
                'ordering': ['-created_on'],
            },
        ),
    ]