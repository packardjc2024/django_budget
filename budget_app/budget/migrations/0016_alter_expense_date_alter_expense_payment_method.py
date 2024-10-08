# Generated by Django 5.1 on 2024-08-30 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0015_alter_expense_line_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default='2024-08-30'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='payment_method',
            field=models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('cash', 'Cash'), ('check', 'Check')], default='credit_card', max_length=11),
        ),
    ]
