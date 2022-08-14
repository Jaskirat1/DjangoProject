# Generated by Django 4.1 on 2022-08-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0002_alter_student_email_alter_student_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='Email:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='First Name:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id:'),
        ),
    ]
