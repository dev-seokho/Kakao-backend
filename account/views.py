import json
import bcrypt
import jwt

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Account
from project_1st.settings import SECRET_KEY

class SignUpView(View):
	def post(self, request):
		data = json.loads(request.body)
		try:
			validate_email(data['email'])
			if len(data['password']) > 7 and len(data['password']) < 33:
				Account.objects.create(
					email = data['email'],
					password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
					name = data['name'],
					birthday = data['birthday'],
					gender = data['gender'],
					lunar = data['lunar'],
				)
				return HttpResponse(status=200)
			return HttpResponse(status=400)

		except ValidationError:
			return HttpResponse(status=400)

		except IntegrityError:
			return HttpResponse(status=400)

		except KeyError:
			return JsonResponse({'message':'INVALID_KEY'}, status=400)

class SignInView(View):
	def post(self, request):
		data = json.loads(request.body)
		try:
			if Account.objects.filter(email = data['email']).exists():
				account = Account.objects.get(email = data['email'])
				if bcrypt.checkpw(data['password'].encode('utf-8'), account.password.encode('utf-8')):
					access_token= jwt.encode({'id': account.id}, SECRET_KEY, algorithm = 'HS256')
					return JsonResponse({'access_token' : access_token.decode('utf-8')}, status=200)
				return HttpResponse(status=401)
			return HttpResponse(status=401)

		except KeyError:
			return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
