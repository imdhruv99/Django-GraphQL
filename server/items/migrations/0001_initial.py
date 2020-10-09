# Generated by Django 3.0.5 on 2020-10-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('doj', models.DateField()),
                ('dob', models.DateField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['-dob'],
            },
        ),
    ]
