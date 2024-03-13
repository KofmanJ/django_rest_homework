from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='payments')
    payment_date = models.DateField(verbose_name='Дата платежа')
    course = models.ForeignKey('tracker.Course', on_delete=models.CASCADE, verbose_name='Курс',
                               related_name='payments', **NULLABLE)
    lesson = models.ForeignKey('tracker.Lesson', on_delete=models.CASCADE, verbose_name='Урок',
                               related_name='payments', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежа')
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('transfer', 'Transfer')],
                                      verbose_name='Способ оплаты')
    payment_url = models.CharField(max_length=500, default='', verbose_name='Ссылка на оплату')
    status = models.CharField(max_length=1, default='P', choices=[("P", "Process"), ("S", "Success"),
                                                                  ("C", "Canceled")], verbose_name='Статус платежа')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f'Пользователь {self.user} оплатил курс {self.course} на сумму {self.amount}'
    