# Generated by Django 3.0.5 on 2020-04-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200423_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pasta',
            field=models.ManyToManyField(related_name='pastas', to='orders.Pasta'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(related_name='pizzas', to='orders.Pizza'),
        ),
        migrations.AlterField(
            model_name='order',
            name='platters',
            field=models.ManyToManyField(related_name='platters', to='orders.DinnerPlatter'),
        ),
        migrations.AlterField(
            model_name='order',
            name='salads',
            field=models.ManyToManyField(related_name='salads', to='orders.Salad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subs',
            field=models.ManyToManyField(related_name='subs', to='orders.Sub'),
        ),
    ]