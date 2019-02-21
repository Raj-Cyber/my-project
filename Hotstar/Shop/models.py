from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='category',blank=True)
    # same img should be referred to Html page(eg:category.img.url)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural= 'categories'
        
    def get_url(self):
        return reverse('Shop:products_by_category',args=[self.slug])



    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product',blank=True)
    # same img should be referred to Html page(eg:products.image.url)
    stock= models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural= 'products'

    def get_url(self):
        return reverse('Shop:ProdCatDetail', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)