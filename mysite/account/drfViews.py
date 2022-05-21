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
        serializer.save()  # 很重要 切记
        if serializer.is_valid():
            return Response(data=data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyAccountView(ModelViewSet):
    queryset = MyAccount.objects.all()
    serializer_class = AccountSerializer
