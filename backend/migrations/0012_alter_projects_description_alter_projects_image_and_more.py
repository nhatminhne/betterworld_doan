# Generated by Django 4.1.1 on 2022-12-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_projects_imagename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='coverBackground',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]