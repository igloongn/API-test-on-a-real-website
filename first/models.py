from django.db import models

# Create your models here.
class UserModel(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40, blank=True, null=True)
    datetime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.firstname 

