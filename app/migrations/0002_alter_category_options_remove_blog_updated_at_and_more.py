# Generated by Django 4.0.5 on 2022-06-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=150),
        ),
    ]
