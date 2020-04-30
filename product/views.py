import json
from django.core import serializers

from django.views import View
from django.http import HttpResponse, JsonResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Theme, Home

class HomeView(View):
	def get(self, request):
		theme_list = Theme.objects.prefetch_related('home_set').all()
		data_list = []
		for theme in theme_list:
			data = {
					"theme_id":theme.id,
					"theme_image":theme.main_image_url,
					"title":theme.name,
					"description":theme.description
			}

			home_list = Home.objects.select_related('product').all()
			product_list = []
			for home in home_list:
				if  home.product is not None:
					if theme.id == home.theme.id:
						product_list.append(
							{
								"image":home.product.image_url,
								"name":home.product.name,
								"price":home.product.price
							}
						)
					data['product'] = product_list
				else:
					pass
			data_list.append(data)
		return JsonResponse({'theme':data_list}, status=200)


class ProductView(View):
	def get(self, request):
		sort_by = request.GET.get("sort_by", None)
		product_list = Product.objects.values('id', 'image_url', 'name', 'price','discount_percentage')
		try:
			if  sort_by == 'hot' :
				return JsonResponse({'hot_product':list(product_list.order_by('-sales_quantity'))}, status=200)
			
			elif sort_by == 'new':
				return JsonResponse({'new_product':list(product_list.order_by('-created_at'))}, status=200)
			
			elif sort_by == 'high_price':
				return JsonResponse({'high_price':list(product_list.order_by('-price'))}, status=200)
			
			elif sort_by == 'low_price': 
				return JsonResponse({'low_price':list(product_list.order_by('price'))}, status=200)
	
			print("end of func")
	
			return HttpResponse(status=400)
		except ValueError:
			return HttpResponse(status=401)

