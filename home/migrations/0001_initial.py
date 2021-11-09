# Generated by Django 3.2.9 on 2021-11-08 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_summery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_calls', models.CharField(max_length=500, null=True)),
                ('Successful_calls', models.CharField(max_length=500, null=True)),
                ('Response_time', models.CharField(max_length=500, null=True)),
                ('Timestamp', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='total_hits',
            fields=[
                ('idd', models.IntegerField(primary_key=True, serialize=False)),
                ('number_calls', models.CharField(max_length=500, null=True)),
                ('Successful_calls', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
