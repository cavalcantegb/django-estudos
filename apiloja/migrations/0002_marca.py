# Generated by Django 2.0.3 on 2019-08-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiloja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('isnMarca', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]
