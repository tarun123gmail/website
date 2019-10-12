from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    pub_date = models.DateField()
    # image = models.ImageField(upload_to='shopping/images', default='')

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50, default='')
    Email = models.CharField(max_length=70, default='')
    Phone = models.IntegerField(default=0)
    Description = models.CharField(max_length=500)
    # sub_date = models.DateField()  hwo to save it in database
    # image = models.ImageField(upload_to='shopping/images', default='')

    def __str__(self):
        return self.First_Name


# Create your models here.
