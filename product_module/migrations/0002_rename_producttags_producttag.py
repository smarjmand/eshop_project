# Generated by Django 4.1.4 on 2023-02-12 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductTags',
            new_name='ProductTag',
        ),
    ]