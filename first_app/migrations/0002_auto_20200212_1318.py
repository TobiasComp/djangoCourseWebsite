# Generated by Django 3.0.3 on 2020-02-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='12345678', max_length=20),
        ),
    ]
