# Generated by Django 4.0.4 on 2022-08-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('italy', '0011_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to='images/'),
        ),
    ]
