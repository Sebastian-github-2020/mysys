from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework_simplejwt import tokens

class CustomAutentication(BaseAuthentication):
    def authenticate(self, request: Request):
        print("自定义认证 校验令牌")
        print(request.META["HTTP_ACCEPT"])
        user = User.objects.get(username="zaks")
        return None
