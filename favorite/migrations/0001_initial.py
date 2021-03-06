# Generated by Django 3.1 on 2020-08-28 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0004_delete_savedproduct'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='food.prod'
                    'uct')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='user',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
