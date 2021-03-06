# Generated by Django 2.0.3 on 2019-08-16 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('html_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='repo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apigihtub.User'),
        ),
    ]
