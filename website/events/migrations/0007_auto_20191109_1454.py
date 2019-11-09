# Generated by Django 2.0.4 on 2019-11-09 14:54

from django.db import migrations, models
import stdnum.ar.cbu


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_update_group_and_perms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccountdata',
            name='account_number',
            field=models.CharField(help_text='Número de cuenta.', max_length=20, verbose_name='número de cuenta'),
        ),
        migrations.AlterField(
            model_name='bankaccountdata',
            name='cbu',
            field=models.CharField(blank=True, help_text='CBU de la cuenta', max_length=317, validators=[stdnum.ar.cbu.validate], verbose_name='CBU'),
        ),
    ]
