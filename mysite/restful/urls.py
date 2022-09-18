
from django.urls import path
from .views import UserApi, UserApiView, UserGenericAPIView,UserListMixinView,UserListMixinView1

urlpatterns = [
    path("users", UserApi.as_view()),  # django.views.view
    path("usersApiView", UserApiView.as_view()),  # rest_framework.views.APIView
    path("usersgenericApiView", UserGenericAPIView.as_view()),  # 通用视图rest_framework.generic.GenericAPIView
    path("usersistMixin", UserListMixinView.as_view()),  # 通用视图rest_framework.generic.GenericAPIView+ListModelMixin
    path("usersistMixin1/<int:pk>", UserListMixinView1.as_view()),  # 通用视图rest_framework.generic.GenericAPIView+ListModelMixin
]
