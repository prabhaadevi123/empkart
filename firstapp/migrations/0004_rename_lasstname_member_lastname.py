# Generated by Django 5.1.2 on 2024-10-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='lasstname',
            new_name='lastname',
        ),
    ]