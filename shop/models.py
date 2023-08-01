from django.db import models

# Create your models here.
category_choices = (
    ('IP', 'I-Phone'),
    ('NK', 'Nokia'),
    ('XI', 'Xiaomi'),
    ('1P', '1Plus'),
    ('ZT', 'ZTE'),
)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True, auto_created=True)
    product_name = models.CharField(max_length=100)
    product_selling_price = models.FloatField()
    product_discounted_price = models.FloatField()
    product_details = models.TextField()
    product_quantity = models.IntegerField()
    product_category = models.CharField(choices=category_choices, max_length=2)
    product_image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product_name

