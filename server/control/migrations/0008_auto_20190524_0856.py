# Generated by Django 2.2 on 2019-05-24 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_somecontroltype_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='somecontrol',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='control_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='somecontrol',
            name='tags',
            field=models.ManyToManyField(related_name='control_tags', to='control.SomeControlTags'),
        ),
        migrations.AlterField(
            model_name='somecontrol',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='control_type', to='control.SomeControlType', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='somecontroltags',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='somecontroltype',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_owner', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]