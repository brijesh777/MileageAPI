# Generated by Django 3.2.7 on 2021-09-29 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vechile', '0006_alter_vechile_mileage_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vechile_mileage',
            name='unit',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='vechile.vechile'),
        ),
    ]
