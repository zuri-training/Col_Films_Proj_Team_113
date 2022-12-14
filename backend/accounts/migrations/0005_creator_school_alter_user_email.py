# Generated by Django 4.1 on 2022-08-13 14:20

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_options_alter_creator_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='school',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='School'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
