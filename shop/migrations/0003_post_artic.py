# Generated by Django 3.1.3 on 2020-11-22 22:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='artic',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
