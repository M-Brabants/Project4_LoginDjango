# Generated by Django 4.1.2 on 2023-01-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='serialNumber',
            field=models.CharField(max_length=50),
        ),
    ]