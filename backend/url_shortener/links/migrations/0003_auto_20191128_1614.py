# Generated by Django 2.2.7 on 2019-11-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20191128_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='short_url',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
