# Generated by Django 4.0.1 on 2022-01-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner_dog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='age',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]