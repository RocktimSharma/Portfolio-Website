# Generated by Django 3.1.6 on 2021-02-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userview', '0003_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUrls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30)),
                ('skill_percentage', models.IntegerField()),
                ('skill_style', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='site_images')),
            ],
        ),
    ]
