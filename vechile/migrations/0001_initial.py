# Generated by Django 3.2.7 on 2021-09-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vechile',
            fields=[
                ('unit', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('mileage', models.IntegerField()),
                ('manufacture', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
