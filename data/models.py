from django.db import models
from django.utils import timezone

class SurveyRes(models.Model):
    name = models.CharField('Как зовут', max_length=64)
    has_money = models.BooleanField('С деньгами', default=False)
    is_generous = models.NullBooleanField('Щедрый')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Результат опроса'
        verbose_name_plural = 'Результаты опросов'

    def __str__(self):
        return self.name