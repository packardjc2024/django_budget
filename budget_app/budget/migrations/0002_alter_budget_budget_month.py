# Generated by Django 5.1 on 2024-08-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_month',
            field=models.CharField(blank=True, max_length=7, null=True, unique=True),
        ),
    ]
