# Generated by Django 3.2 on 2021-05-06 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210506_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]