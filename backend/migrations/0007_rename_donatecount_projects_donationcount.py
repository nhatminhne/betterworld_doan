# Generated by Django 4.1.1 on 2022-12-08 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_contribution_projectid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='donateCount',
            new_name='donationcount',
        ),
    ]