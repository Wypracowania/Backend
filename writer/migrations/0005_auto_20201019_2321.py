# Generated by Django 3.1.1 on 2020-10-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0004_bid_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='writerimage',
            name='image',
            field=models.ImageField(unique=True, upload_to='pisarz'),
        ),
    ]
