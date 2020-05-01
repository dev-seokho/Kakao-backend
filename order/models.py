from django.db import models

class DeliveryStatus(models.Model):
        name = models.CharField(max_length=20)
        account_deliverystatus = models.ManyToManyField('account.Account', through='Order')

        class Meta:
            db_table = 'delivery_status'

class Order(models.Model):
        order_number = models.CharField(max_length=45)
        payment_method = models.CharField(max_length=10)
        address = models.CharField(max_length=100)
        detail_address = models.CharField(max_length=100)
        shopping_charge = models.IntegerField(default=0)
        point = models.IntegerField(default=0)
        message = models.CharField(max_length=50)
        created_at = models.DateTimeField(auto_now_add=True)
        payment_amount = models.IntegerField(default=0)
        account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
        delivery_status = models.ForeignKey('DeliveryStatus', on_delete=models.SET_NULL, null=True)
        product_order = models.ManyToManyField('product.Product', through='product.ProductOrder')

        class Meta:
            db_table = 'orders'

class Basket(models.Model):
        quantity = models.IntegerField(default=0)
        order_status = models.BooleanField(default=0)
        account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
        product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'baskets'
