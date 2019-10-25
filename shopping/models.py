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


class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    Item_json = models.CharField(max_length=5000)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    timestamp = models.DateField(auto_now_add=True)
    update_desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.update_desc[0:9] + '...'


# Create your models here.
