# Generated by Django 4.0.4 on 2022-06-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('Username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
