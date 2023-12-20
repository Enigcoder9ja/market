from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'



class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.fname} {self.lname}'



class Product(models.Model):
    name =  models.CharField(max_length=50)
    price =  models.DecimalField(max_length=50, default=0, decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description =  models.CharField(max_length=300, default='', blank=True, null=True)
    image =  models.ImageField(upload_to='upload/product/')

    #sale section

    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_length=50, default=0, decimal_places=2, max_digits=10)


    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=150, default='', blank=True, )
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(datetime.datetime.today)
    status = models.BooleanField(default=False)



    def __str__(self):
        return self.product