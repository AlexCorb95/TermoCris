# Generated by Django 4.1 on 2022-09-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_short_desc',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
