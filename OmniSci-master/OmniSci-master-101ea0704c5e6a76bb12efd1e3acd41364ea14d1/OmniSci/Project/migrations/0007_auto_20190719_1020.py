# Generated by Django 2.1.7 on 2019-07-19 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0006_auto_20190719_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='projection_introduction',
            field=models.TextField(max_length=5000, verbose_name='项目介绍'),
        ),
    ]