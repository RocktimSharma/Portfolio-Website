# Generated by Django 3.1.6 on 2021-03-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0006_auto_20210301_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='codeLink',
            field=models.URLField(blank=True),
        ),
    ]
