# Generated by Django 5.1 on 2024-09-12 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0021_alter_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default='2024-09-12'),
        ),
    ]
