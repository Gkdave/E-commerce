from django.db import models
from base.models import BaseModel
from django.utils.text import slugify 



class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self,*args ,**kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save() 

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,related_name='porducts')
    price = models.IntegerField()
    product_description = models.TextField()
    #color_variant = models.ManyToManyField(color_variant,blank=True)
    #size_variant = models.ManyToManyField(SizeVariant,black=True)



class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images') 
    image = models.ImageField(upload_to="product")