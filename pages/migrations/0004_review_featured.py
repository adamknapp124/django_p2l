# Generated by Django 4.1.2 on 2022-10-19 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_value_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]