# Generated by Django 4.1.3 on 2022-11-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_status_read_status_book_unique_book_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='read_status',
            field=models.CharField(max_length=50),
        ),
    ]
