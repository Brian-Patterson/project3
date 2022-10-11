# Generated by Django 4.1.2 on 2022-10-10 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('strength', models.IntegerField(max_length=2)),
                ('dexterity', models.IntegerField(max_length=2)),
                ('constitution', models.IntegerField(max_length=2)),
                ('intelligence', models.IntegerField(max_length=2)),
                ('wisdom', models.IntegerField(max_length=2)),
                ('charisma', models.IntegerField(max_length=2)),
                ('hitPoints', models.IntegerField(max_length=3)),
            ],
        ),
    ]