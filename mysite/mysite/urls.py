"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework_simplejwt.authentication
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from . import settings
# 配置api 文档
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="接口文档",
        default_version='1.0.0',
        description="描述信息",
        contact=openapi.Contact(email="xxxx@gmail.com"),
        license=openapi.License(name="版本协议")
    ),
    public=True,  # 允许所有人访问
    # permission_classes=[IsAuthenticated],  # 权限类
    authentication_classes=[rest_framework_simplejwt.authentication.JWTAuthentication]
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
                  path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 图片路径设置
                  path("djangoapi/", include('restful.urls')),  # api 接口

                  path('account/', include('account.urls')),
                  # path('doc', include_docs_urls(title="api文档", description="django rest framework")),
                  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 生成令牌  用户名 密码登录，
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('', admin.site.urls),
                  path("mdeditor/", include("mdeditor.urls")),  # markdown编辑器
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 注意 这一行，在django 4.0 不需要加就能显示media 图片

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
