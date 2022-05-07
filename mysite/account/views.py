from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import MyAccount
from django.db.models import Q


# Create your views here.
def accounts(request: HttpRequest, search_key=None):
    """
    查询账户信息
    """
    print("参数", search_key)
    if search_key is None:
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
    else:
        """
        查询条件不为空 以描述和账户名作为查询 选项
        """
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

        # ac = MyAccount.objects.filter(account_description__contains=search_key).values()
        # ac_number = ac.count()
        # if ac_number > 0:
        #     # print("账户描述",list(ac))
        #     return JsonResponse({
        #         'status': 200,
        #         'data': list(ac),
        #         'msg': ''
        #     }, safe=False, )
        # else:
        #     ac = MyAccount.objects.filter(account_name__contains=search_key).values()
        #     count = ac.count()
        #     if count > 0:
        #         print("账户名")
        #         return JsonResponse({
        #             'status': 200,
        #             'count':count,
        #             'data': list(ac),
        #             'msg': ''
        #
        #         }, safe=False, )
        #
        # return JsonResponse({
        #     'status': 200,
        #         'data': None,
        #         'msg': '没有数据'
        # })
