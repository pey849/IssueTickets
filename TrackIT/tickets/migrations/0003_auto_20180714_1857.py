# Generated by Django 2.0.6 on 2018-07-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_tickets_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='slug',
            new_name='foo',
        ),
    ]