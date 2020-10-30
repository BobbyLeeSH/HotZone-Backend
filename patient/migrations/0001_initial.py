# Generated by Django 3.1.2 on 2020-10-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('national_id', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
