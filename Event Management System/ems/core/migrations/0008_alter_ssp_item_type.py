# Generated by Django 5.1.4 on 2025-01-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_vendoreventassignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssp',
            name='item_type',
            field=models.CharField(choices=[('Furniture', 'Furniture'), ('Decor', 'Decor'), ('Stage', 'Stage'), ('Setup', 'Setup'), ('Entrance', 'Entrance'), ('Services', 'Services'), ('Audio-Visual', 'Audio-Visual'), ('Stalls', 'Stalls'), ('Lighting', 'Lighting'), ('Miscellaneous', 'Miscellaneous')], max_length=50),
        ),
    ]
