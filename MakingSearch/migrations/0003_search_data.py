# Generated by Django 2.2.4 on 2019-09-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MakingSearch', '0002_auto_20190901_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
