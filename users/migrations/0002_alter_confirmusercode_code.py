# Generated by Django 4.1.7 on 2023-04-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmusercode',
            name='code',
            field=models.IntegerField(max_length=6),
        ),
    ]