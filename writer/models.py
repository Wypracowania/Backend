from django.db import models
from user.models import Order
from django.contrib.auth.models import User

# Create your models here.

class Bid(models.Model):
    order   = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=300)
    price   = models.IntegerField(default=20)
    writer  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.order.topic + " Bid"

class WriterImage(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image  = models.ImageField(upload_to="pisarz", unique=True)
    
    def __str__(self):
        return self.writer.username + " photo"
