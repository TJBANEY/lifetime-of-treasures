# Generated by Django 2.1.7 on 2019-07-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190308_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(default='', max_length=700),
        ),
    ]
