from django.db import models

class MainCategory(models.Model):
        name = models.CharField(max_length=45)
        image_url = models.URLField(max_length=2000)

        class Meta:
    	    db_table = 'main_categories'


class SubCategory(models.Model):
        name = models.CharField(max_length=45)
        main_category = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'sub_categories'

class SeriesCategory(models.Model):
        name = models.CharField(max_length=20)
        image_url = models.URLField(max_length=2000)

        class Meta:
            db_table = 'series_categories'

class Theme(models.Model):
        name = models.CharField(max_length=45)
        main_image_url = models.URLField(max_length=2000)
        detail_image_url = models.URLField(max_length=2000)
        description = models.CharField(max_length=1000)
        product_theme = models.ManyToManyField('Product', through='ProductTheme')

        class Meta:
    	    db_table = 'themes'

class Home(models.Model):
        theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'homes'

class Home(models.Model):
	theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

	class Meta:
		db_table = 'homes'

class Character(models.Model):
        image_url = models.URLField(max_length=2000)
        name = models.CharField(max_length=20)
        description = models.TextField()
        product_character = models.ManyToManyField('Product', through='ProductCharacter')

        class Meta:
            db_table = 'characters'

class NewImage(models.Model):
        name = models.CharField(max_length=50)
        image_url = models.URLField(max_length=2000)
        description = models.CharField(max_length=300)

        class Meta:
            db_table = 'new_images'

class Product(models.Model):
        name = models.CharField(max_length=50)
        price = models.IntegerField(default=0)
        detail = models.TextField()
        sub_detail = models.TextField()
        stock =  models.IntegerField(default=0)
        image_url = models.URLField(max_length=2000)
        created_at = models.DateTimeField()
        global_delivery = models.BooleanField(default=1)
        sales_quantity = models.IntegerField(default=0)
        discount = models.BooleanField(default=1)
        discount_percentage = models.DecimalField(max_digits=10, decimal_places=2)
        series_category = models.ForeignKey('SeriesCategory', on_delete=models.SET_NULL, null=True)
        account_product_basket = models.ManyToManyField('account.Account', through='order.Basket')
        maincategory_product = models.ManyToManyField('MainCategory', through='ProductCategory')
        hot_image = models.OneToOneField('HotImage', on_delete=models.SET_NULL, null=True)

        class Meta:
    	    db_table = 'products'

class ProductOrder(models.Model):
        quantity = models.IntegerField(default=0)
        order = models.ForeignKey('order.Order', on_delete=models.SET_NULL, null=True)
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_orders'

class Image(models.Model):
        image_url = models.URLField(max_length=2000)
        product = models.ForeignKey('product', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'images'

class HotImage(models.Model):
        image_url = models.URLField(max_length=2000)

        class Meta:
            db_table = 'hot_images'

class Size(models.Model):
        name = models.CharField(max_length=100)
        product_size = models.ManyToManyField('Product', through='ProductSize')

        class Meta:
            db_table = 'sizes'

class Color(models.Model):
        name = models.CharField(max_length=30)
        product_color = models.ManyToManyField('Product', through='ProductColor')

        class Meta:
            db_table = 'colors'

class Review(models.Model):
        score = models.FloatField()
        comment = models.TextField
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now_add=True)
        account_id = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'reviews'

class ReviewLike(models.Model):
        review = models.ForeignKey('Review', on_delete=models.SET_NULL, null=True)
        account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'review_likes'

class ProductTheme(models.Model):
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
        theme = models.ForeignKey('Theme', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_themes'

class ProductSize(models.Model):
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
        size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_sizes'

class ProductColor(models.Model):
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
        color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_colors'

class ProductCharacter(models.Model):
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
        character = models.ForeignKey('Character', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_characters'

class ProductCategory(models.Model):
        product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
        main_category = models.ForeignKey('MainCategory', on_delete=models.SET_NULL, null=True)
        sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)

        class Meta:
            db_table = 'products_categories'
