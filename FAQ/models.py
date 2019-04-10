from django.db import models

# Create your models here.
class FAQItems(models.Model):
    content = models.TextField()
