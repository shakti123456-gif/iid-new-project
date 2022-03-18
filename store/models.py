from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from payu.models import Transaction
from account.models import Account
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


class Item(models.Model):
    title=models.CharField(max_length=100,verbose_name="Product Name")
    price=models.FloatField()
    description1=models.CharField(max_length=200,blank=True,null=True)
    description2=RichTextField(default="Product Description",null=True,blank=True)   
    slug=models.SlugField(blank=True,null=True)

    images=models.ImageField(upload_to="",null=True,blank=True,help_text='Image resolution must be 600px x 600px')

    class Meta:
        verbose_name = 'Product'
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        
        return reverse("store:products", kwargs={"slug": self.slug})

    def add_to_cart(self):

        return reverse("store:add-to-cart",kwargs={'slug':self.slug})
    
    def get_remove_from_cart(self):
        return reverse("store:remove",kwargs={'slug':self.slug})

    def clean(self):
        w,h=get_image_dimensions(self.images)
        
        
        file_size=self.images.file.size

        if file_size >50000:
            raise ValidationError("Size of the image must be > 50 KB and < 2 MB")

        if file_size >2000000:
             raise ValidationError("Size of the image must be < 2 MB and > 50 KB")

        if w<600 or w>600 and h<600 or h>600:
            raise ValidationError("Image resolution must be 600px x 600px")

class KingOrderItems(models.Model):

    item=models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True,related_name="orderitems")
    quantity=models.IntegerField(default=1)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,related_name="user2")
    ordered=models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ordered List'
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}" 
    
    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_final_price(self):

        return self.get_total_item_price()


CATEGORY_CHOICES1=(

    ('Processing','Processing'),
    ('Completed','Completed'),
    ('Active','Active'),
)


class KingOrder(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="user3",blank=True, null=True)
    items=models.ManyToManyField(KingOrderItems,related_name="orders")
    ordered_date=models.DateTimeField(blank=True, null=True)
    ordered=models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, blank=True, null=True)
    invoice = models.FileField(upload_to='Invoice/', null=True, blank=True)
    billing_address=models.ForeignKey('BillingAddress',on_delete=models.SET_NULL,blank=True,null=True)
    shipment=models.CharField(choices=CATEGORY_CHOICES1,max_length=100,default="Active",blank=True,null=True)
    Tracking_field=models.URLField(blank=True,null=True)    
       
    def __str__(self):
        return str(self.user)
    
    def get_total(self):
        total=0

        for i in self.items.all():
            total+=i.get_total_item_price()

        return total
    
    class Meta:
        verbose_name = 'Ordered Product'
        verbose_name_plural = 'Ordered Products'


class BillingAddress(models.Model):
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,null=True,blank=True)        
    address_1=models.CharField(max_length=200,null=True)
    address_2=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    zip_code=models.CharField(max_length=100,null=True)
    check=models.BooleanField(default=True)
    
    def __str__(self):
    
        return str(self.name)

    class Meta:
        verbose_name = 'Billing Address'
        verbose_name_plural = 'Billing Address'
