# Generated by Django 2.0.3 on 2019-08-16 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apigihtub', '0002_auto_20190816_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repo',
            old_name='user_id',
            new_name='id',
        ),
    ]
