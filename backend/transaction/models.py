from django.db import models
from django.utils.timezone import now


class TransactionType(models.Model):
    """Тип операции"""

    TYPE_CHOICES = [
        ('business', 'Пополнение'),
        ('personal', 'Списание'),
        ('tax', 'Налог'),
    ]

    name = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        blank=False,
        verbose_name="Название статуса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Категория"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Категория"
    )
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип операции"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """Подкатегория"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Подкатегория"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class TransactionStatus(models.Model):
    """Статус транзакции"""

    name = models.CharField(
        max_length=50,
        #choices=STATUS_CHOICES,
        blank=False,
        verbose_name="Название статуса"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус транзакции"
        verbose_name_plural = "Статусы транзакций"



class Transaction(models.Model):
    """Транзация, модель со всеми составляющими"""

    STATUS_CHOICES = [
        ('business', 'Бизнес'),
        ('personal', 'Личное'),
        ('tax', 'Налог'),
    ]

    created_at = models.DateField(
        default=now,
        verbose_name="Дата создания записи"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='personal',
        verbose_name="Статус"
    )
    transaction_type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="Тип операции"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="Категория"
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name="Подкатегория"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма"
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий"
    )

    def __str__(self):
        return f"{self.created_at} - {self.amount} руб."

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
