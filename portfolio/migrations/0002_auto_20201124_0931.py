# Generated by Django 3.1.2 on 2020-11-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/images'),
        ),
    ]