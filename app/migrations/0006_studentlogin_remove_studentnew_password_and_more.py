# Generated by Django 4.2.4 on 2023-08-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_adminlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentnew',
            name='password',
        ),
        migrations.RemoveField(
            model_name='studentnew',
            name='userid',
        ),
    ]
