# Generated by Django 4.2.4 on 2023-08-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0005_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Изображение'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
