# Generated by Django 4.0.5 on 2022-06-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='name',
        ),
        migrations.AddField(
            model_name='director',
            name='d_name',
            field=models.CharField(default='unknown', max_length=100, verbose_name='Director'),
        ),
    ]
