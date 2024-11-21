# Generated by Django 4.2.16 on 2024-11-15 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_featured', models.BooleanField(default=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='featured_product', to='shop.product')),
            ],
        ),
    ]
