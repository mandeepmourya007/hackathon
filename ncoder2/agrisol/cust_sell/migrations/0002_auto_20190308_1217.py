# Generated by Django 2.1.7 on 2019-03-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust_sell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='static/seller/images'),
        ),
    ]
