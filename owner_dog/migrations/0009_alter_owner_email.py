# Generated by Django 4.0.1 on 2022-01-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner_dog', '0008_alter_dog_age_alter_owner_age_alter_owner_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]