from rest_framework import serializers
from .models import MyAccount


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAccount
        fields = '__all__'
        # 非必填 只读字段
        read_only_fields = ['create_date', 'modify_date', 'id']
        # 给字段添加额外的约束
        extra_kwargs = {
            "account_description": {
                "error_messages": {
                    "required": "账户描述必填"
                }
            },
            "account_name": {
                "min_length": 6,
                "error_messages": {
                    "min_value": "用户名最少6位",
                    "max_value": "用户名最长50位",
                    "required": "账户必填"
                },

            },
            "account_password": {
                "min_length": 6,
                "error_messages": {
                    "min_value": "密码最少6位",
                    "max_value": "密码最长50位",
                    "required": "密码必填"
                },
            }
        }

    def validate(self, attrs):
        """反序列化的时候对所有字段进行自定义校验"""
        return attrs

    #  方法名 validate_【字段名称】
    def validate_account_name(self, account_name):
        """对指定的字段进行校验 执行顺序在 全部字段校验前面"""
        return account_name
