# Generated by Django 5.1.4 on 2025-01-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_vendoreventassignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
