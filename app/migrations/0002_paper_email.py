# Generated by Django 3.2 on 2021-06-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
