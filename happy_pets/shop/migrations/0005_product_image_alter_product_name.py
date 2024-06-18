# Generated by Django 5.0.6 on 2024-06-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_rename_delivered_order_is_ordered_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]