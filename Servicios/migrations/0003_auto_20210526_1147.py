# Generated by Django 3.1.7 on 2021-05-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_auto_20210511_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
