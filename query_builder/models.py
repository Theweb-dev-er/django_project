from django.db import models

class year_class(models.Model):
    class_year = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    
# Create your models here.
