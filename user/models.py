from django.db import models
from django.contrib.auth.models import User
# from writer.models import Writer
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
    owner    = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    document = models.CharField(max_length=3, choices=DOCUMENT_CHOICES, default='ESE')
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='')
    topic    = models.CharField(max_length=100, blank=False, default='')
    pages    = models.IntegerField(default=1)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    instructions = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.topic

class OrderInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')
    paid = models.BooleanField(default=False)
    assigned_writer = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    completed = models.BooleanField(default=False)
    value = models.IntegerField(default=0)
    completed_order = models.FileField(upload_to="completed", unique=True, null=True)
    date_completed = models.DateField(null=True)

    def __str__(self):
        return self.order.topic


class Conversation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    writer = models.ForeignKey("writer.Writer", on_delete=models.CASCADE, default='')

    def unreaded_messages(self):
        all_messages = Message.objects.filter(conversation=self)
        unreaded_messages = 0

        for message in all_messages:
            if message.readed == False and message.author != self.customer:
                unreaded_messages += 1
        return unreaded_messages
    
    def last_message(self):
        all_messages = Message.objects.filter(conversation=self)
        if all_messages:
            last_message = all_messages[len(all_messages)-1]
            return str(last_message.text[0:22])
        else:
            return ""

    def last_sended(self):
        all_messages = Message.objects.filter(conversation=self)
        if all_messages:
            last_message = all_messages[len(all_messages)-1]
            return last_message.created_at
        else:
            return ""




class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, default='')
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    readed = models.BooleanField(default=False)