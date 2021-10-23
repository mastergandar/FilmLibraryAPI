# Generated by Django 3.2.8 on 2021-10-23 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_auto_20211023_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiskName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='No name', max_length=255, null=True, verbose_name='Disk name')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='disk_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='films.diskname'),
        ),
    ]