# Generated by Django 2.0.7 on 2018-10-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0008_auto_20181011_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_timer',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
