# Generated by Django 3.2.18 on 2023-03-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
