# Generated by Django 2.2.28 on 2023-03-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20230317_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
