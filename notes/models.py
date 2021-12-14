from django.db import models
from datetime import date


class Note(models.Model):
	title = models.CharField('Title', max_length=100)
	text = models.CharField('Text', max_length=1000, null=True, blank=True)
	owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notes', verbose_name='Owner')
	created_on = models.DateField('Created On', default=date.today)

	def __str__(self):
		return self.title
	