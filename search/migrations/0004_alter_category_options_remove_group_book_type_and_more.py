# Generated by Django 4.0 on 2021-12-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_remove_category_meta_remove_group_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='book_type',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('UN', 'Unspecified'), ('TU', 'Tutorial'), ('RS', 'Research'), ('RW', 'Review')], default='UN', max_length=2),
        ),
        migrations.AddField(
            model_name='group',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='search.Category'),
        ),
    ]
