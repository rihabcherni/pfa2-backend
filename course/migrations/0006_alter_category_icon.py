# Generated by Django 4.1.13 on 2024-03-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_category_course_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(default='0xe148', max_length=100),
        ),
    ]
