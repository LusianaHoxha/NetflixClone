# Generated by Django 4.1.4 on 2022-12-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='ivdeos',
        ),
        migrations.AddField(
            model_name='movie',
            name='vdeos',
            field=models.ManyToManyField(to='core.video'),
        ),
    ]