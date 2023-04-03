# Generated by Django 4.0.3 on 2023-04-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0002_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='type',
            field=models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10),
        ),
    ]
