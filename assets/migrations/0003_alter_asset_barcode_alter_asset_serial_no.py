# Generated by Django 4.0.5 on 2022-06-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_alter_delivery_options_delivery_in_transit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='barcode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial_no',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
