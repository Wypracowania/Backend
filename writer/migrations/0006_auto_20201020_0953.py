# Generated by Django 3.1.1 on 2020-10-20 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0005_auto_20201019_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='image',
            new_name='photo',
        ),
    ]
