# Generated by Django 2.0.3 on 2019-08-07 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiloja', '0009_maquina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maquina',
            old_name='isnPlacaVideo',
            new_name='isnMaquina',
        ),
    ]
