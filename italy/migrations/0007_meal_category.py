# Generated by Django 4.0.4 on 2022-08-07 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('italy', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='italy.category'),
        ),
    ]
