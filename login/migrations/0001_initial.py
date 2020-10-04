# Generated by Django 3.1.2 on 2020-10-03 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Course1', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=150, null=True)),
                ('Course2', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=150, null=True)),
                ('Course3', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=150, null=True)),
            ],
        ),
    ]