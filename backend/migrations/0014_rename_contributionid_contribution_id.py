# Generated by Django 4.1.1 on 2022-12-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_rename_contributionid_contribution_contributionid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='contributionId',
            new_name='id',
        ),
    ]
