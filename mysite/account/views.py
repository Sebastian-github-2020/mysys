from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MyAccount
from django.db.models import Q


# Create your views here.
@csrf_exempt
def accounts(request: HttpRequest):
    """
    查询账户信息
    1. get方式获取所有的 账户信息
    2. post方式 查询
    """
    # 请求方式
    method = request.method
    print("请求方式",method)
    if method == 'GET':
        """
            查询所有账户
        """
        ac = MyAccount.objects.all().values()
        print("阿萨大大撒旦", ac.count())
        count = ac.count()
        if count > 0:
            return JsonResponse({
                'status': 200,
                'data': list(ac),
                'msg': ''
            }, safe=False, )
        else:
            return JsonResponse({
                'status': 200,
                'data': None,
                'msg': '没有数据'
            })
    elif method == 'POST':
        # 注意 request.POST 只能读取表单的数据 不能读取json参数
        body = json.loads(request.body)
        print(body)
        search_key = body.get('search_key')


        """
        查询条件不为空 以描述和账户名作为查询 选项
        """
        if search_key is not None:
            ac = MyAccount.objects.filter(
                Q(account_description__contains=search_key) | Q(account_name__contains=search_key)).values()
            count = ac.count()
            if count > 0:
                return JsonResponse({
                    'status': 200,
                    'count': count,
                    'data': list(ac),
                    'msg': ''
                }, safe=False, )
            else:
                return JsonResponse({
                    'status': 200,
                    'count': count,
                    'data': None,
                    'msg': '没有数据'
                })

        else:
            return JsonResponse({
                'status': 200,
                "flag":"参数为空",
                'data': None,
                'msg': '没有数据'
            })