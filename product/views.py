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
			if  sort_by == 'hot' :
				return JsonResponse({'products':list(product_list.order_by('-sales_quantity'))}, status=200)
			
			elif sort_by == 'new':
				return JsonResponse({'products':list(product_list.order_by('-created_at'))}, status=200)
			
			elif sort_by == 'high_price':
				return JsonResponse({'products':list(product_list.order_by('-price'))}, status=200)
			
			elif sort_by == 'low_price': 
				return JsonResponse({'products':list(product_list.order_by('price'))}, status=200)
	
			return HttpResponse(status=400)
		except ValueError:
			return HttpResponse(status=401)


		
