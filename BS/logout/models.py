from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.username
