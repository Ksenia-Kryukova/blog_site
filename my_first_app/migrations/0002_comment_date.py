# Generated by Django 5.1.3 on 2024-12-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Date',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
    ]