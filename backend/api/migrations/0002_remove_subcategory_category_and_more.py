# Generated by Django 4.2.18 on 2025-01-16 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_type',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='TransactionType',
        ),
    ]
