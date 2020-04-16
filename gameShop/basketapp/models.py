from django.db import models

from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created_at = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return self.user
    
    def get_price_all(self):
        return self.product.price * self.quantity


    