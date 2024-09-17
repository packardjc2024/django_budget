# Generated by Django 5.1 on 2024-08-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_alter_budget_budget_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('merchant', models.CharField(max_length=20)),
                ('line_item', models.CharField(choices=[('Gas', 'Gas'), ('Food', 'Food'), ('Internet', 'Internet'), ('Phone', 'Phone'), ('Electric', 'Electric'), ('Trash', 'Trash'), ('Mortgage', 'Mortgage'), ('Child Care', 'Child Care'), ('Insurance', 'Insurance')], default='Food', max_length=20)),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit'), ('Debit Card', 'Debit'), ('Cash', 'Cash'), ('Check', 'Check')], default='Credit Card', max_length=11)),
                ('budget_month', models.CharField(choices=[('August', 'August')], max_length=7)),
            ],
        ),
    ]
