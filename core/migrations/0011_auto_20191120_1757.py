# Generated by Django 2.2.7 on 2019-11-20 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191120_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontreiro',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Concluída'), (2, 'Cancelada')], default=0, verbose_name='Situação'),
        ),
    ]
