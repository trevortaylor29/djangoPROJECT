# Generated by Django 4.1.4 on 2022-12-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_pizza_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image_url',
            field=models.URLField(),
        ),
    ]
