# Generated by Django 4.0.5 on 2022-07-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_submission_submission_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_ID',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
