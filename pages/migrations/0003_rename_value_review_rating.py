# Generated by Django 4.1.2 on 2022-10-19 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_review_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='value',
            new_name='rating',
        ),
    ]