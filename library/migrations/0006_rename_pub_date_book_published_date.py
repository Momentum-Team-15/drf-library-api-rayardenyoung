# Generated by Django 4.1.3 on 2022-11-09 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_status_options_alter_status_read_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_date',
            new_name='published_date',
        ),
    ]
