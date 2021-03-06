# Generated by Django 2.1.3 on 2018-11-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Found',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=250)),
                ('FinderName', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=250)),
                ('OwnerName', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=250)),
                ('OwnerName', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
