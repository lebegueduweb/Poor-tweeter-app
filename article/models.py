from django.db import models
import datetime
from django.utils import timezone



class Article(models.Model):
    article_heading = models.CharField(max_length=200)
    article_body = models.TextField(max_length=50)
    date = models.DateField(("Date"), default=datetime.date.today)
    article_id = models.AutoField(primary_key=True)
