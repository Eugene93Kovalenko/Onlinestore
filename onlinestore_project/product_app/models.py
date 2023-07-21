from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=20)
    money = models.CharField(max_length=20, default='asd')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"


text = 'asd'
