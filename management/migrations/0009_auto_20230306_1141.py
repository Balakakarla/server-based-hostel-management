# Generated by Django 3.2.18 on 2023-03-06 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_newregistration_requester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.room'),
        ),
    ]