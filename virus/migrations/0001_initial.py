# Generated by Django 3.1.2 on 2020-10-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('common_name', models.CharField(max_length=30)),
                ('maximum_period_of_infection', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
