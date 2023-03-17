# Generated by Django 2.2.28 on 2023-03-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20230316_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_description',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingrediants',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_steps',
            field=models.CharField(default='', max_length=2000),
        ),
    ]