# Generated by Django 2.2.20 on 2021-04-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210416_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='basket',
            field=models.ManyToManyField(related_name='baskets', to='recipes.Ingredient'),
        ),
    ]