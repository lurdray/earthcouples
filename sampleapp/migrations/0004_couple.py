# Generated by Django 2.2.4 on 2020-03-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_auto_20191008_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Couple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hus_name', models.CharField(max_length=20)),
                ('wife_name', models.CharField(max_length=20)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
