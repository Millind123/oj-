# Generated by Django 4.0.5 on 2022-07-03 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_submission_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
