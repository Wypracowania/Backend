from django.db import models

# Create your models here.

class Order(models.Model):
    DOCUMENT_CHOICES = [
        ('ESE', 'Esej'),
        ('WYP', 'Wypracowanie'),
	]
    CATEGORY_CHOICES = [
		('PRZ', 'Nauki przyrodnicze'),
		('HUM', 'Nauki humanistyczne'),
		('ŚCI', 'Nauki ścisłe'),
	]
    document = models.CharField(max_length=3, choices=DOCUMENT_CHOICES, default='ESE')
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='')
    topic = models.CharField(max_length=100, blank=False, default='')
    pages = models.IntegerField(default=1)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.topic