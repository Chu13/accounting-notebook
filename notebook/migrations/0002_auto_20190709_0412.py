# Generated by Django 2.2.3 on 2019-07-09 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='kind',
            new_name='type',
        ),
    ]
