# Generated by Django 3.1 on 2020-08-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_delete_savedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutriscore_grade',
            field=models.CharField(default='x', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default='https://world.openfoodfacts.org/'),
        ),
    ]
