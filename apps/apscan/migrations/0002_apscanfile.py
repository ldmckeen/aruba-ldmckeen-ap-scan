# Generated by Django 4.1.5 on 2023-02-01 14:18
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('apscan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APScanFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
