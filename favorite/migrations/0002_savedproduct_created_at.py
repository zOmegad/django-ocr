# Generated by Django 3.1 on 2021-05-31 22:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
