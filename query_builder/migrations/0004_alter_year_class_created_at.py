# Generated by Django 4.2.1 on 2023-05-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_builder', '0003_alter_year_class_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year_class',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
