# Generated by Django 3.0.6 on 2020-06-24 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_request_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
