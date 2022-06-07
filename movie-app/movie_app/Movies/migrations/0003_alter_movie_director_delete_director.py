# Generated by Django 4.0.5 on 2022-06-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_remove_director_name_director_d_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default='unknown', max_length=100, verbose_name='Director'),
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]
