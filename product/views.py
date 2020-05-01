import json

from django.views          import View
from django.http           import HttpResponse, JsonResponse
from .models               import HotImage, NewImage, Product, Image, MainCategory, SubCategory, ProductCategory

class HotImageView(View):
    def get(self, request):

        popular_images = HotImage.objects.all().values()

        return JsonResponse({'all_popular_image':list(popular_images)}, status=200)

class NewImageView(View):
    def get(self, request):

        new_images = NewImage.objects.all().values()

        return JsonResponse({'all_new_image':list(new_images)}, status=200)

class NewProductView(View):
    def get(self, request):

        product_all = Product.objects.all().order_by('-created_at')
        product_main = product_all.values('id','name','price','image_url')
        return JsonResponse({'product_new_main':list(product_main)}, status=200)

class SaleProductView(View):
    def get(self, request):

        product_discount = Product.objects.filter(discount=True)
        product_discount_list = list(product_discount)

        discount_list=[]

        for i,v in enumerate(product_discount.values('id','name','image_url','price','discount_percentage')):
            if i!=0 and i!=1 and i !=2:
                discount_list.append(v)

        return JsonResponse({'sale_item':discount_list}, status=200)

class MainSalePrductView(View):
    def get(self, request):

        product_discount = Product.objects.filter(discount=True)
        product_discount_list = list(product_discount)

        discount_list=[]

        for i,v in enumerate(product_discount.values('id','name','image_url','price','discount_percentage')):
            if i==0 or i==1 or i ==2:
                discount_list.append(v)

        return JsonResponse({'sale_item':discount_list}, status=200)

class ProductInformationView(View):
    def get(self, request, products_id):

        information_images = Image.objects.filter(product_id=products_id).values('image_url')
        product_information = Product.objects.filter(id=products_id).values('id','name','price','detail','sub_detail')

        information_images_list = list(information_images)
        product_information_list = list(product_information)

        all_information = product_information_list+information_images_list

        return JsonResponse({'information':all_information} , status=200)

class CategoryView(View):
    def get(self, request):

        category = MainCategory.objects.prefetch_related('subcategory_set')
        category_list=[{i.name:list(i.subcategory_set.values('id','name'))}for i in category]

        return JsonResponse({'category':category_list}, status=200)

class SubCategoryView(View):
    def get(self, request, sub_id):

        all=ProductCategory.objects.select_related('product').filter(sub_category_id=sub_id)
        all_list = [{"id":a.product.id, "name":a.product.name, "price":a.product.price, "image_url":a.product.image_url}for a in all]

        return JsonResponse({'product':all_list}, status=200)
