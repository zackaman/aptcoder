# Generated by Django 3.1.2 on 2020-10-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Course2',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Course3',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=150, null=True),
        ),
    ]
