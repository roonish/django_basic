from django.db import models

class Promotion(models.Model):
     desc = models.CharField(max_length=255)
     discount = models.FloatField()

class Collection(models.Model):
     title = models.CharField(max_length=255)
    #  not to create reverse relation use + on related_name
     featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=3)
    # if auto_now_add it will only update it for the first time it was created
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)



class Customer(models.Model):
     MEMBERSHIP_BRONZE = 'B'
     MEMBERSHIP_GOLD = 'G'
     MEMBERSHIP_SILVER = 'S'

     MEMBERSHIP_CHOICES = [
          (MEMBERSHIP_BRONZE,'bronze'),
          (MEMBERSHIP_GOLD,'gold'),
          (MEMBERSHIP_SILVER,'silver'),
     ]
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255) 
     email = models.EmailField(unique=True)
     phone = models.CharField(max_length=255)
     birth_Date = models.DateField(max_length=100,null=True)
     membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

class Order(models.Model):
     ORDER_PENDING = 'P'
     ORDER_COMPLETE = 'C'
     ORDER_fAILED = 'F'

     ORDER_STATUS = [
          (ORDER_PENDING,'order pending'),
          (ORDER_COMPLETE,'order complete'),
          (ORDER_fAILED,'order failed')
     ]
     placed_at = models.DateTimeField(auto_now=True)
     payment_status = models.CharField(max_length=1,choices=ORDER_STATUS, default=ORDER_PENDING)
     customer = models.ForeignKey (Customer,on_delete=models.PROTECT)
#implement one to one relationship
# class Address(models.Model):
#      city = models.CharField(max_length=255)
#      customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

#one to many    
class Address(models.Model):
     city = models.CharField(max_length=255)
     customer = models.ForeignKey (Customer,on_delete=models.CASCADE)

class Cart(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     
class OrderItem(models.Model):
     order = models.ForeignKey(Order, on_delete=models.PROTECT)
     product = models.ForeignKey(Product,on_delete=models.PROTECT)
     quantity = models.PositiveBigIntegerField()
     unit_price = models.DecimalField(max_digits=5,decimal_places=2)

class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     quantity = models.PositiveBigIntegerField() 