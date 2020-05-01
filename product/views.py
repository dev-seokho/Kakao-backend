import json
from django.core import serializers

from django.views import View
from django.http import HttpResponse, JsonResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Theme, Home

class HomeView(View):
	def get(self, request):
		home_theme = [{
			'theme_id':theme.id,
			'theme_image':theme.main_image_url,
			'title':theme.name,
			'description':theme.description,
			'product':[{
				'image':product.product.image_url,
				'name':product.product.name,
				'price':product.product.price
			}for product in Home.objects.select_related('theme', 'product').filter(theme__id = theme.id) if product.product]
		}for theme in Theme.objects.prefetch_related('home_set').all()]
		return JsonResponse({'theme':home_theme}, status=200)


class ProductView(View):
	def get(self, request):
		sort_by = request.GET.get("sort_by", None)
		product_list = Product.objects.values('id', 'image_url', 'name', 'price','discount_percentage')
		try:
			entire_product ={
				'hot':list(product_list.order_by('-sales_quantity')),
				'new':list(product_list.order_by('-created_at')),
				'high_price':list(product_list.order_by('-price')),
				'low_price':list(product_list.order_by('price'))
			}
			for key in entire_product:
				if sort_by == key:
					return JsonResponse({'product':entire_product[sort_by]}, status=200)
				return HttpResponse(status=400)
			return HttpResponse(status=400)
		
		except ValueError:
			return HttpResponse(status=401)


		
