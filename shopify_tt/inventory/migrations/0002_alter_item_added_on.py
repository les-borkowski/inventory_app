# Generated by Django 4.0.5 on 2022-06-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
