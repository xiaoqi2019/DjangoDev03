"""DjangoDev03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# 全局路由配置信息
# 1：urlpatterns为固定名称的列表
# 2：列表中的一个元素，代表一条路由信息
# 3：从上往下匹配，如果可以匹配上，Django会自动调用path函数的第二个参数指定的视图（函数视图）
# 4：如果匹配不上，会自动抛出404异常（默认为404.状态码为404）
# 5：一旦匹配成功，不会继续往下匹配
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("projects.urls")),
    path("", include("interfaces.urls")),
    path("", include("testsuits.urls")),
    path("", include("reports.urls")),
    path("", include("envs.urls")),
    path("", include("testcases.urls")),
    path("", include("debugtalks.urls")),
    path("", include("configures.urls")),
    path("", include("summary.urls")),
    path("docs/", include_docs_urls(title="测试平台接口文档")),
    path("api/", include("rest_framework.urls")),  # 使用DRF框架自带的登入和登出的页面
    path("user/", include("users.urls"))
]
