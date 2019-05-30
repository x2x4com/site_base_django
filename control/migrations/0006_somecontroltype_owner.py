# Generated by Django 2.2 on 2019-05-24 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control', '0005_auto_20190524_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='somecontroltype',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]