from io import BytesIO
from django.core.files import File
from PIL import Image


def resize_image(image, size=(120, 120)):

    im = Image.open(image)

    im.convert('RGB') # convert mode

    im.thumbnail(size) # resize image

    thumb_io = BytesIO() # create a BytesIO object

    im.save(thumb_io, 'JPEG', quality=85) # save image to BytesIO object

    thumbnail = File(thumb_io, name=image.name) # create a django friendly File object

    return thumbnail