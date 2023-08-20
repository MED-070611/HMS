# Generated by Django 3.1.5 on 2021-01-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Mobile', models.CharField(max_length=13)),
                ('Email', models.EmailField(blank=True, max_length=70)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
