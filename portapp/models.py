from django.db import models

class Port(models.Model):
    title = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='media/',blank=True)
    description = models.TextField(blank=True)
    
    url =models.URLField(blank=True)
    port_title =models.CharField(max_length=100,blank=True)
    
    def __str__(self): 
        return self.title
        
    


