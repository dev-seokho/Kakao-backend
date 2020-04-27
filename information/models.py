from django.db import models

class Privacy(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        db_table = 'privacies'

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = 'notices'

class QuestionType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'question_types'

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    question_type = models.ForeignKey('QuestionType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'faqs'

class StoreDistrict(models.Model):
    name = models.CharField(max_length=50)
    storecountry_storedistrict = models.ManyToManyField('StoreCountry', through='Store')

    class Meta:
        db_table = 'store_districts'

class StoreCountry(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'store_countries'

class Store(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    business_hours = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length= 2000)
    store_country = models.ForeignKey('StoreCountry', on_delete=models.SET_NULL, null=True)
    store_district = models.ForeignKey('StoreDistrict', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'stores'


