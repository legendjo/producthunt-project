from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Django Models Field Documentation:
https://docs.djangoproject.com/en/3.1/ref/models/fields/
'''
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')
    icon =  models.ImageField(upload_to='images/')
    votesTotal= models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + ('...')

    def pub_date_refined(self):
        return self.pub_date.strftime('%b %w, %Y')
        #https://strftime.org/
        #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
