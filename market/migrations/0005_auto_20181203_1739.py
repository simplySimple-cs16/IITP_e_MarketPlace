# Generated by Django 2.1.3 on 2018-12-03 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_buysell_curruser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buysell',
            old_name='currUser',
            new_name='userName',
        ),
    ]