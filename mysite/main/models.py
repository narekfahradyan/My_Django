from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=50)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=40)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='home_images')
    slug = models.SlugField('Product slug', unique=True)
    about = models.TextField('Product about')

class Cart(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)