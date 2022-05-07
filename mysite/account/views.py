from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import MyAccount


# Create your views here.
def accounts(request: HttpRequest, account_description: str = None, account_name: str = None):
    """
    查询账户信息
    """
    ac = MyAccount.objects.all().values()

    # print(list(ac))
    return JsonResponse(list(ac),safe=False)