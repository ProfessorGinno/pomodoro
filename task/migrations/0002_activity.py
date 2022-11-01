# Generated by Django 4.1.2 on 2022-11-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('creation_date', models.DateField()),
                ('advance_percentage', models.FloatField()),
            ],
        ),
    ]
