# Generated by Django 4.1.6 on 2023-02-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_rename_create_vacancy_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
