# Generated by Django 2.2 on 2019-05-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_remove_somecontrol_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='somecontroltags',
            name='refer',
        ),
        migrations.AddField(
            model_name='somecontrol',
            name='tags',
            field=models.ManyToManyField(to='control.SomeControlTags'),
        ),
    ]