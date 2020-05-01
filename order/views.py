import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Basket
from account.models import Account
from account.utils import login_required

class BasketView(View):
	@login_required
	def get(self, request):
		cart_data = Basket.objects.filter(account = request.user.id).select_related('product')
		basket = []
		for cart in cart_data:
			cart_list = {
				"image":cart.product.image_url,
				"name":cart.product.name,
				"quantity":cart.quantity,
				"price":cart.product.price
			}
			if cart.product.discount == 1:
				cart_list["discount_percentage"]=cart.product.discount_percentage  
			basket.append(cart_list)
		return JsonResponse({'basket':basket}, status=200)
	
	@login_required
	def post(self, request):
		data = json.loads(request.body)
		cart_data = Basket.objects.filter(account = request.user.id)
		try:
			if Basket.objects.filter(product=data['product_id']).exists():
				cart_data = Basket.objects.get(account = request.user.id)
				cart_data.quantity += 1
				cart_data.save()
			
			else:
				Basket.objects.create(
					account_id = request.user.id,
					product_id = data['product_id'],
					quantity = data['quantity'])
			return HttpResponse(status=200)
		
		except KeyError:
			return JsonResponse({'message':'INVALID_KEY'}, status=400)

