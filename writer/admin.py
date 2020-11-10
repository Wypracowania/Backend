from django.contrib import admin
from .models import (
    Bid, 
    # WriterImage, 
    Categories, 
    Writer,
    # WriterDetails, 
    # Review,
    Rating
)
# Register your models here.

admin.site.register(Bid)
# admin.site.register(WriterImage)
admin.site.register(Categories)
admin.site.register(Writer)
# admin.site.register(Review)
admin.site.register(Rating)