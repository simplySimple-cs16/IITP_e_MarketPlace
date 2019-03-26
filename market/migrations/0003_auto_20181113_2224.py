# Generated by Django 2.1.3 on 2018-11-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_found_lost_rent'),
    ]

    operations = [
        migrations.CreateModel(
            name='To_Let',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=250)),
                ('OwnerName', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('ChargesPerDay', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.RenameField(
            model_name='rent',
            old_name='OwnerName',
            new_name='Rentee',
        ),
    ]
