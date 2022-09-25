from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50,default= "" )
    product_des = models.CharField(max_length=400)
    price = models.IntegerField(default=0)
    product_date = models.DateField()
    prod_image = models.ImageField(upload_to = "ekart/images" , default ="")
    
    
    def __str__(self):
        return self.product_name
    