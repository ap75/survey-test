from django.db import models

class SurveyRes(models.Model):
    name = models.CharField('Как зовут', max_length=64)
    has_money = models.BooleanField('С деньгами', default=False)
    is_generous = models.NullBooleanField('Щедрый')
