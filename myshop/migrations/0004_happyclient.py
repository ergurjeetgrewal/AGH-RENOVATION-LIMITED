# Generated by Django 3.0.7 on 2020-06-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='happyclient',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('review', models.TextField()),
            ],
        ),
    ]
