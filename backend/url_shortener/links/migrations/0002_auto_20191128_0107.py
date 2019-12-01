# Generated by Django 2.2.7 on 2019-11-27 23:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='short_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='links',
            name='lifetime_days',
            field=models.IntegerField(blank=True, default=90),
        ),
        migrations.AlterField(
            model_name='links',
            name='original_url',
            field=models.CharField(max_length=300),
        ),
    ]
