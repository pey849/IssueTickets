# Generated by Django 2.0.6 on 2018-07-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]