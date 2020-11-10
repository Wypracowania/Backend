from django.db import models
from user.models import Order
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Categories(models.Model):
    CATEGORIES = [
		('PRZ', 'Nauki przyrodnicze'),
		('HUM', 'Nauki humanistyczne'),
		('ŚCI', 'Nauki ścisłe'),
	]
    category = models.CharField(max_length=3, choices=CATEGORIES, default='')


class WriterDetails(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='')
    description = models.CharField(max_length=300, default='')
    categories = models.ManyToManyField(Categories, default='')
    # rating = models.ForeignKey(Rating, on_delete=models.CASCADE, default='', null=True)


class Writer(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='')
    categories = models.ManyToManyField(Categories, default='')
    description = models.CharField(max_length=300, default='')
    # photo = models.ForeignKey(WriterImage, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="pisarz", unique=True, null=True)
    completed_order = models.IntegerField(default=0)

    def rate(self):
        all_objects = Rating.objects.filter(worker=self)
        count = 0
        average = 0
        for x in all_objects:
            count += 1
            average += x.rate
        if count == 0:
            return average
        return average/count

    def total_rates(self):
        all_objects = Rating.objects.filter(worker=self)
        count = 0
        for x in all_objects:
            count += 1
        return count

    def __str__(self):
        return self.writer.username

class Rating(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    worker = models.ForeignKey(Writer, on_delete=models.CASCADE, default='')
    opinion = models.CharField(max_length=130, default='')
    rate = models.FloatField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])


class Bid(models.Model):
    order   = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=300)
    price   = models.IntegerField(default=20)
    writer_details = models.ForeignKey(Writer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.order.topic + " Bid"

