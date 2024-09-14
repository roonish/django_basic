# Generated by Django 5.1.1 on 2024-09-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_2e448d_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customer',
        ),
    ]
