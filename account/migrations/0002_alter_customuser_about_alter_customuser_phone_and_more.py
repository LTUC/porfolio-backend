# Generated by Django 4.1 on 2022-09-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="about",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="theme",
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
