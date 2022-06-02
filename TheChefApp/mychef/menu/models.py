from django.db import models

# Create your models here.
class MenuAttribute(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='menu_imgs/')
    price=models.IntegerField(default=0)