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


class Sneakers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='sneakers/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_make = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'


class Blouse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='blouses/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_make = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Кофта'
        verbose_name_plural = 'Кофты'


class Pants(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='pants/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_make = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Штаны'
        verbose_name_plural = 'Штаны'


class Socks(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    photo = models.ImageField(upload_to='socks/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_make = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Носки'
        verbose_name_plural = 'Носки'


class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.CharField(max_length=100, verbose_name='Содержимое')
    photo = models.ImageField(upload_to='blogs/', verbose_name='Превью', **NULLABLE)
    date_make = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
