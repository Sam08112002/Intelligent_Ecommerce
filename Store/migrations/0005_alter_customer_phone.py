# Generated by Django 5.1.1 on 2024-09-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0004_customer_alter_product_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=15),
        ),
    ]