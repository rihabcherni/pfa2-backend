# Generated by Django 4.1.13 on 2024-03-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='otp',
            field=models.CharField(default='1234', max_length=4),
        ),
    ]
