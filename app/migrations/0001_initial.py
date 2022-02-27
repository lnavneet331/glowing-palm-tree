# Generated by Django 4.0 on 2022-02-27 05:32

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
                ('name', models.CharField(max_length=64)),
                ('organizer', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=32)),
                ('period', models.CharField(max_length=32)),
                ('amount', models.IntegerField(max_length=10)),
                ('application_fees', models.IntegerField(max_length=5)),
                ('description', models.IntegerField(max_length=512)),
            ],
        ),
    ]
