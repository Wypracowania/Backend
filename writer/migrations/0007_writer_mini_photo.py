# Generated by Django 3.1.1 on 2020-11-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0006_auto_20201111_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='mini_photo',
            field=models.ImageField(null=True, upload_to='pisarz'),
        ),
    ]
