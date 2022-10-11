# Generated by Django 4.1.2 on 2022-10-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_app', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='background',
            field=models.CharField(default='background', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='job',
            field=models.CharField(default='background', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(default='background', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='skillProficiency',
            field=models.CharField(default='background', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='subrace',
            field=models.CharField(default='background', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(default='background', max_length=100),
        ),
    ]
