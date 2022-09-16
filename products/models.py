from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    product_short_desc = models.CharField(max_length=300)
    product_description = models.TextField(max_length=1000)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_img = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f'{self.product_name}'
