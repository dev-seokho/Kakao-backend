import jwt
import json

from django.http import JsonResponse

from .models import Account
from project_1st.settings import SECRET_KEY

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({'error_code':'INVALID_LOGIN'})

        encode_token = request.headers["Authorization"]

        try:
            data = jwt.decode(encode_token, SECRET_KEY, algorithm = 'HS256')
            user = Account.objects.get(email = data['email'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({'error_code':'INVALID_TOKEN'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'error_code':'UNKNOWN_USER'}, status=401)

        return func(self, request, *args, **kwargs)

    return wrapper

