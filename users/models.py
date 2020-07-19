from django.db import models
      
class Signup(models.Model):
    username = models.CharField( max_length = 50)
    email = models.CharField(max_length = 120)
    password = models.CharField(max_length = 100)
    password2 = models.CharField(max_length = 100)
    def __str__(self):
        return self.firstname+self.lastname