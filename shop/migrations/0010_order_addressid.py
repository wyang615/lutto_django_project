# Generated by Django 2.1.1 on 2018-10-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20181024_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='addressid',
            field=models.IntegerField(null=True),
        ),
    ]
