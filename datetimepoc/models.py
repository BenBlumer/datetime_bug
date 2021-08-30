from django.db import models

# Create your views here.

class Order(models.Model):
    intake_date_and_time = models.DateTimeField(blank=True, null=True)