# Generated by Django 4.0 on 2021-12-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_category_group_variant_remove_book_book_types_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='group',
            name='description',
        ),
        migrations.RemoveField(
            model_name='group',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='features',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='price',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='status',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='values',
        ),
    ]
