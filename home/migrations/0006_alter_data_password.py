# Generated by Django 3.2.9 on 2021-11-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]