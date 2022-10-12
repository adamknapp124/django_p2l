# Generated by Django 4.1.2 on 2022-10-12 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.TextField(null=True),
        ),
    ]
