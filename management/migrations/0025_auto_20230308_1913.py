# Generated by Django 3.2.18 on 2023-03-08 13:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_expenses_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.PositiveIntegerField(default=300, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(30000)]),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DateToDateReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.CharField(max_length=100, null=True)),
                ('to_date', models.CharField(max_length=100, null=True)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(30000)])),
                ('expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.expenses')),
                ('fee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.fee')),
            ],
        ),
    ]