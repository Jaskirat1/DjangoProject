# Generated by Django 4.1 on 2022-08-10 07:58

from tabnanny import verbose
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
    ]
