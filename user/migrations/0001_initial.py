# Generated by Django 3.1.1 on 2020-09-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(choices=[('ESE', 'Esej'), ('WYP', 'Wypracowanie')], default='ESE', max_length=3)),
                ('category', models.CharField(choices=[('PRZ', 'Nauki przyrodnicze'), ('HUM', 'Nauki humanistyczne'), ('ŚCI', 'Nauki ścisłe')], default='', max_length=3)),
                ('topic', models.CharField(default='', max_length=100)),
                ('pages', models.IntegerField(default=1)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
