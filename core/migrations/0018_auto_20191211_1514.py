# Generated by Django 2.2.7 on 2019-12-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20191211_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipeazul',
            name='encontristas',
        ),
        migrations.AddField(
            model_name='equipeazul',
            name='encontristas',
            field=models.ManyToManyField(to='core.Encontrista'),
        ),
    ]
