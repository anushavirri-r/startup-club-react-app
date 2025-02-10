# Generated by Django 3.1.7 on 2021-03-22 18:19

import Frontend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_post_drivelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(
                blank=True, null=True, upload_to=Frontend.models.upload_path),
        ),
    ]
