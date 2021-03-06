# Generated by Django 2.2.7 on 2019-11-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20191120_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontreiro',
            name='bairro_encontreiro',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='encontreiro',
            name='logradouro_encontreiro',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='encontrista',
            name='bairro',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='encontrista',
            name='logradouro',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Logradouro'),
        ),
    ]
