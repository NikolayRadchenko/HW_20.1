from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_make = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
