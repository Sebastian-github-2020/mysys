from rest_framework import serializers
from account.models import MyAccount


# 定义基本序列化器

class UserSerializer(serializers.Serializer):
    """
    基础序列化器，这里传入的参数都是为了反序列化：客户端传入的json->模型对象 校验
    1. 注意这里的所有的属性默认都是required =True
    """
    id = serializers.IntegerField(required=False, read_only=True)  # read_only只读 客户端不能修改
    account_description = serializers.CharField(max_length=100, label='描述', required=False)
    account_name = serializers.CharField(max_length=50, label='账户名')
    account_password = serializers.CharField(max_length=50, label='密码')
    create_date = serializers.DateTimeField(label='创建日期', required=False)
    modify_date = serializers.DateTimeField(label='修改日期', required=False)
    email = serializers.CharField(max_length=100, label='邮箱', required=False)
    phone = serializers.CharField(max_length=20, label='手机号', required=False)

    def create(self, validated_data):
        return MyAccount.objects.create(**validated_data)

    def update(self, instance: MyAccount, validated_data):
        instance.account_name = validated_data.get("account_name")
        instance.save()
        return instance

    def validate(self, attrs):
        # 对所有字段校验
        return attrs

    # 验证单个字段  validate_xxx
    def validate_account_name(self, data: str):
        # 对account_name进行校验
        len_num = len(data)
        if 6 < len_num < 20:
            return data
        else:
            raise serializers.ValidationError(detail="长度不合法", code=666)


#

class UserModelSerializer(serializers.ModelSerializer):
    # 可以声明自定义字段

    class Meta:
        # 指定模型 --必填
        model = MyAccount
        # 字段列表  - 必填
        # fields = "__all__"  # 模型的全部字段
        fields = ["account_name", "email", "account_description", "id", "account_password"]  # 可显示给前端的字段   序列化的字段
        # exclude = ["account_password"]
        # 选填字段--只在序列化阶段 使用的字段  id 不能被前端修改
        read_only_fields = ["id"]
        # 选填 字段的额外约束
        extra_kwargs = {
            "min_length": 6,
            "account_name": {
                "error_messages": {
                    "required": "账户名必填",
                    "min_value": "用户名长度小于6"
                }
            }
        }

    def create(self, validated_data):
        return MyAccount.objects.create(**validated_data)

    def update(self, instance: MyAccount, validated_data):
        instance.account_name = validated_data.get("account_name")
        instance.save()
        return instance

    def validate(self, attrs):
        # 对所有字段校验
        return attrs

    # 验证单个字段  validate_xxx
    def validate_account_name(self, data: str):
        # 对account_name进行校验
        len_num = len(data)
        if 6 < len_num < 20:
            return data
        else:
            raise serializers.ValidationError(detail="长度不合法", code=666)
