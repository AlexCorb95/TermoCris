from datetime import datetime

from django.db import models

from products.models import Products
from userextend.models import UserExtend


class ShoppingCart(models.Model):
    user = models.ForeignKey(UserExtend, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now)


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)


    def __str__(self):
        return self.product


