# Generated by Django 2.2 on 2019-05-06 08:02

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('cms', '0003_contentpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentindexpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='intro'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='intro',
            field=models.CharField(max_length=250, verbose_name='intro'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='body'),
        ),
        migrations.CreateModel(
            name='ContentPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='cms.ContentPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
