# Generated by Django 4.0 on 2022-03-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=64)),
                ('providedby', models.CharField(default='Unknown', max_length=64)),
                ('eligibilitycriteria', models.CharField(default='Unknown', max_length=512)),
                ('exam', models.CharField(default='Unknown', max_length=64)),
                ('scholarshipamount', models.CharField(default='Unknown', max_length=18)),
                ('applicationfees', models.CharField(default='Unknown', max_length=18)),
                ('deadline', models.CharField(default='Unknown', max_length=32)),
                ('link', models.URLField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=256)),
                ('message', models.TextField(max_length=4098)),
            ],
        ),
    ]
