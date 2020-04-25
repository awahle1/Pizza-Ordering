# Generated by Django 3.0.5 on 2020-04-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200423_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pasta',
            field=models.ManyToManyField(related_name='orders', to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='order',
            name='platters',
            field=models.ManyToManyField(related_name='orders', to='orders.DinnerPlatter'),
        ),
        migrations.AddField(
            model_name='order',
            name='salads',
            field=models.ManyToManyField(related_name='orders', to='orders.Salad'),
        ),
        migrations.AddField(
            model_name='order',
            name='subs',
            field=models.ManyToManyField(related_name='orders', to='orders.Sub'),
        ),
    ]