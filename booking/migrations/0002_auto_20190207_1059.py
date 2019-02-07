# Generated by Django 2.1.5 on 2019-02-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='chair_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='username',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]