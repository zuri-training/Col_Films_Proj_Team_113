from django.db import models

# Create your models here.
# class Faq(models.Model):
#     question = models.TextField()
#     answer = models.TextField()   

class Faq(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
    
class Faq_D(models.Model):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name='faqs')
    description = models.TextField()