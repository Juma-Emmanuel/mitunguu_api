# Generated by Django 5.0.6 on 2024-05-21 16:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitunguu_app', '0002_product_location_product_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
