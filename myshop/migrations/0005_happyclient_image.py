# Generated by Django 3.0.7 on 2020-06-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_happyclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='happyclient',
            name='image',
            field=models.ImageField(default='', upload_to='myshop/clients'),
        ),
    ]