# Generated by Django 4.2.16 on 2024-11-15 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_is_featured_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
