# Generated by Django 4.2.18 on 2025-01-16 11:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Подкатегория')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тип операции')),
            ],
            options={
                'verbose_name': 'Тип операции',
                'verbose_name_plural': 'Типы операций',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания записи')),
                ('status', models.CharField(choices=[('business', 'Бизнес'), ('personal', 'Личное'), ('tax', 'Налог')], default='personal', max_length=20, verbose_name='Статус')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='api.category', verbose_name='Категория')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='api.subcategory', verbose_name='Подкатегория')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='api.transactiontype', verbose_name='Тип операции')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='transaction_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='api.transactiontype', verbose_name='Тип операции'),
        ),
    ]
