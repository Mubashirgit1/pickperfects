from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    sku = models.CharField(max_length=254, null=True, blank=True)

    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    has_sizes = models.BooleanField(default=False,null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # ⭐ Fields for AI gift recommendations
    tags = models.JSONField(null=True, blank=True)
    occasion = models.JSONField(null=True, blank=True)
    recipient = models.CharField(max_length=50, null=True, blank=True)

    def get_sale_percentage(self):
        if not self.tags:
            return None

        for tag in self.tags:
            if isinstance(tag, (int, float)):
                return int(tag)
            if isinstance(tag, str):
                raw = tag.strip().replace('%', '')
                if raw.isdigit():
                    return int(raw)

        return None

    def get_discounted_price(self):
        sale_pct = self.get_sale_percentage()
        if sale_pct is None or sale_pct <= 0:
            return self.price

        from decimal import Decimal
        discount = (Decimal(sale_pct) / Decimal(100)) * self.price
        return (self.price - discount).quantize(Decimal('0.01'))

    def __str__(self):
        return self.name