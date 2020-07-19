from django.db import models
      
class ContactUs(models.Model):
    firstname = models.CharField( max_length = 50)
    lastname = models.CharField( max_length = 50)
    email = models.CharField(max_length = 120)
    contactno = models.CharField(max_length = 12)
    query = models.TextField(max_length = 256)
    def __str__(self):
        return self.firstname