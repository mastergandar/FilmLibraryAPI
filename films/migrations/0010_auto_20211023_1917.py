# Generated by Django 3.2.8 on 2021-10-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_auto_20211023_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='disk_name',
            field=models.CharField(blank=True, default='No name', max_length=255, null=True, verbose_name='Disk name'),
        ),
        migrations.DeleteModel(
            name='DiskName',
        ),
    ]
