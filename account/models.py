from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    agreement = models.BooleanField(default=1)
    address = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)
    point = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    gender =  models.CharField(max_length=100)
    birthday =  models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    lunar = models.BooleanField(default=1)
    account_product_review = models.ManyToManyField('product.Product', through='product.Review')
    account_review = models.ManyToManyField('product.Review', through='product.ReviewLike')
    class Meta:
        db_table = 'accounts'

class Country(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'contries'

class QNA(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    question = models.TextField()
    image_url = models.URLField(max_length=2000)
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = 'qnas'

