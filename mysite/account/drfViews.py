from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import AccountSerializer
from .models import MyAccount
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


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
