from django.db import models

from apps.common.models import BaseModel

from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', related_query_name='product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Discount (%)'))
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def real_price(self):
        if self.discount == 0 or self.discount is None:
            return self.price
        return self.price - (self.price * self.discount / 100)