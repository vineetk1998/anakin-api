# Generated by Django 3.2.13 on 2022-06-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstore',
            name='promotion',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, unique=True),
        ),
    ]
