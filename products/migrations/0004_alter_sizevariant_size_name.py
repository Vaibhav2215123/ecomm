# Generated by Django 4.1.5 on 2023-03-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_size_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizevariant',
            name='size_name',
            field=models.IntegerField(default=0),
        ),
    ]
