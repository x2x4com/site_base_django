# Generated by Django 2.2 on 2019-05-24 08:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_somecontroltype_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='somecontroltype',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='create_time'),
            preserve_default=False,
        ),
    ]