# Generated by Django 4.0 on 2021-12-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_alter_category_options_remove_group_book_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='type',
        ),
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.CharField(choices=[('UN', 'Unspecified'), ('TU', 'Tutorial'), ('RS', 'Research'), ('RW', 'Review')], default='UN', max_length=2),
        ),
    ]
