from django.db import models
from django.utils import timezone

class Record(models.Model):
    date = models.DateTimeField('date published')
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    brightness = models.FloatField(default=0)
    img_url = models.CharField(max_length=200)

r = Record(date = timezone.now(), temperature = 20.1, humidity = 50, brightness = 1000, img_url="prova")
r.save()

Record.objects.all()
