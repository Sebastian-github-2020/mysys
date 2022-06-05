from rest_framework import status
from rest_framework.generics import GenericAPIView  # 通用视图
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView  # 基本视图类
from rest_framework.viewsets import ModelViewSet

from .models import MyAccount
from .serializers import AccountSerializer

"""基本视图类"""


class MyAccountAPIView(APIView):

    def get(self, request: Request):
        """
        获取全部数据
        注意：由模型->字典是序列化 不用验证   直接传值进去 不用data=data这样
        :param request:
        :return:
        """
        print("进入了")
        data = MyAccount.objects.all()

        serializer = AccountSerializer(data, many=True).data

        return Response(data=serializer, status=status.HTTP_200_OK)


def post(self, request: Request):
    """
    创建账户
    :param request:
    :return:
    """
    data = request.data
    print("post", data)
    # 將传入的数据 存入数据库，这属于反序列化  需要验证格式
    serializer = AccountSerializer(data=data)

    if serializer.is_valid():
        serializer.save()  # 很重要 切记
        return Response(data=data)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 基本视图类
class MyAccountInfoAPIView(APIView):
    def get(self, request: Request, account_id: int):
        """
        获取一条用户信息
        :param request:
        :param account_id:
        :return:
        """
        try:
            account = MyAccount.objects.get(id=account_id)
        except MyAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 序列化
        serializer = AccountSerializer(instance=account)

        # 返回结果
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, account_id: int):
        """
        更新数据
        :param request:
        :param account_id: 账户id
        :return:
        """
        # 获取客户端提交的数据
        data = request.data
        # 查询需要更新的数据
        account = MyAccount.objects.get(id=account_id)
        # 反序列化
        serializer = AccountSerializer(instance=account, data=data)
        # 验证
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, account_id):
        """删除数据"""
        pass


class MyAccountView(ModelViewSet):
    """这种做法不常用,不能满足需求"""
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer


# 通用视图类,如 查询 所有 用户 ，查询所有影片 代码是一样的 ，所以使用通用代码 只写一次

class MyAccountGenericView(GenericAPIView):
    queryset = MyAccount.objects.all()  # 指定查询集
    serializer_class = AccountSerializer  # 指定序列化器

    def get(self, request: Request):
        """获取所有账户信息"""
        account_list = self.get_queryset()
        serializer = self.get_serializer(instance=account_list, many=True)
        return Response(serializer.data, 200)

    def post(self, request: Request):
        """创建一条数据"""
        serializer = self.get_serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, 200)
        else:
            return Response(serializer.errors)


class MyAccountInfoGenericView(GenericAPIView):
    serializer_class = AccountSerializer
    queryset = MyAccount.objects.all()  # 指定查询集
    lookup_field = "id"  # 设置查询的 键  不设置 就默认是pk  ,注意 url参数和 函数参数 这里要一致  是pk都是pk 是id都是id

    def get(self, request: Request, id):
        """获取单个信息"""

        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data, 200)

    def put(self, request, id):
        """更新一个数据"""
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        else:
            return Response(serializer.errors)


"""视图拓展类"""
from rest_framework.mixins import ListModelMixin  # 获取多条数据 返回响应结果
from rest_framework.mixins import CreateModelMixin  # 添加一条数据 返回响应结果
from rest_framework.mixins import RetrieveModelMixin  # 获取一条数据  返回响应结果
from rest_framework.mixins import UpdateModelMixin  # 更新数据 （全部字段更新）  返回响应结果
from rest_framework.mixins import DestroyModelMixin  # 删除一条字段  返回响应结果


# 配合通用视图
class MyAccountListMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer

    def get(self, request: Request):
        """查询所有账户数据"""
        return self.list(request=request)

    def post(self, request: Request):
        """添加一条数据"""
        return self.create(request=request)


class MyAccountMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer

    def get(self, request: Request, pk):
        """
        获取一条数据
        :param request:
        :param pk:
        :return:
        """
        return self.retrieve(request=request, pk=pk)

    def put(self, request, pk):
        """
        更新一条数据  更新全部字段
        :param request:
        :param pk:
        :return:
        """
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        """
        删除一条数据
        :param request:
        :param pk:
        :return:
        """
        return self.destroy(request, pk=pk)


"""
视图子类是  通用视图类和视图拓展的子类
"""
from rest_framework.generics import CreateAPIView  # GenericAPIView+CreateModelMixin  组合 添加一条数据 的视图
from rest_framework.generics import ListAPIView  # GenericAPIView +ListModelMixin 获得多条数据 的视图

"""组合视图"""


class MyAccountCreateApiView(CreateAPIView):
    pass


class MyAccountListApiView(ListAPIView, CreateAPIView):
    """获取多条数据 + 创建数据"""
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer


"""视图集  解决上面的重复性代码,和视图很类似 区别在于 方法名"""
from rest_framework.viewsets import ViewSet, ModelViewSet


# 和上面的apiView代码类似 可以多继承  minx
class MyAccountViewSet(ViewSet):
    pass


# 装饰器
from rest_framework.decorators import action


class MyAccountModelViewSet(ModelViewSet):
    """
    1. 生成5个查询，如果不需要这么多 可以选择其他的 视图集继承
    2. 但是api不可能只有这5个  需要添加的话需要用到 装饰器
    """
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "id"

    # detail 代表是否需要指定一个pk参数 来获取唯一的数据  这个参数可以指定的  看上面
    @action(methods=["get"], detail=True, url_path="login")
    def login(self, request, id):
        r = self.retrieve(request=request, id=id)

        r.data = {
            "msg": "登录成功",
            "data": [r.data]
        }
        print(r.data)
        return r

    @action(methods=["PATCH"], detail=True, url_path="modify")
    def modify_pwd(self, request, id):
        """局部更新"""
        res = self.partial_update(request=request, id=id)
        return res
