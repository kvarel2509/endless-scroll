from django.db import models


class Word(models.Model):
	title = models.CharField('Слово', max_length=30)
	description = models.TextField('Описание')
