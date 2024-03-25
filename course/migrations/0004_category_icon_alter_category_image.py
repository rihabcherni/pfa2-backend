# Generated by Django 4.1.13 on 2024-03-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_courseprogressscore_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='category', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='assets/category/autre.PNG', upload_to='assets/category'),
        ),
    ]
