# Generated by Django 3.1.7 on 2021-06-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='students',
            field=models.ManyToManyField(to='users.user'),
        ),
    ]
