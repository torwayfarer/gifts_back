# Generated by Django 2.2.7 on 2019-11-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20191113_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='CityMobil',
            new_name='Collage',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='GetTaxi',
            new_name='DreamArt',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Uber',
            new_name='Electronic_design',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Yandex',
            new_name='Print_no_edit',
        ),
        migrations.AddField(
            model_name='form',
            name='size',
            field=models.CharField(max_length=120),
        ),
    ]