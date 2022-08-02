from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    
    
        
	