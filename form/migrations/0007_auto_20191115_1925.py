# Generated by Django 2.2.7 on 2019-11-15 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20191115_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='size_of_picture',
            new_name='size',
        ),
    ]
