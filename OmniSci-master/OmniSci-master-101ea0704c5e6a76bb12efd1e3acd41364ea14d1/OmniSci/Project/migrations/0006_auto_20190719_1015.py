# Generated by Django 2.1.7 on 2019-07-19 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_auto_20190716_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='projection_introduction',
            field=models.CharField(max_length=50000, verbose_name='项目介绍'),
        ),
    ]
