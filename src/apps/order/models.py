from django.db import models

from apps.common.models import BaseModel
from apps.product.models import Product

from django.utils.translation import gettext_lazy as _


class Order(BaseModel):
    STATUS_CHOICES = (
        (0, _('Pending')),
        (1, _('Confirmed')),
        (2, _('Delivered')),
        (3, _('Canceled')),
    )

    telegram_user = models.ForeignKey('user.TelegramUser', on_delete=models.CASCADE, related_name='orders', related_query_name='order')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    notes = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def total(self):
        return sum([item.price for item in self.cart_items.all()])
    
    @property
    def subtotal(self):
        return sum([item.discount for item in self.cart_items.all()])


class CartItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', related_query_name='cart_item')
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_items', related_query_name='cart_item')

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
        
    @property
    def price(self):
        return self.product.price * self.quantity
    
    @property
    def discount(self):
        return self.product.real_price * self.quantity
