# Generated by Django 3.2.11 on 2022-01-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='json_file',
            field=models.FileField(blank=True, null=True, upload_to='address_json/'),
        ),
    ]