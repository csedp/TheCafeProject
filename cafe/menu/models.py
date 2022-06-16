from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=20)

class Menu(models.Model):
    dishName = models.CharField(max_length=20)
    dishDesc = models.TextField()
    dishPrice = models.IntegerField()
    dishPrepTime= models.IntegerField()
    dishImage= models.ImageField(upload_to='menu_imgs/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)