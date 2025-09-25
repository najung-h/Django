"""
URL configuration for firstpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# include 추가합니다.
from django.urls import path, include
from articles import views

# 프로젝트의 urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    # 클라이언트로 부터 http://127.0.0.1:8000/articles/ 요청이 들어오면
    # articles 앱의 views 모듈의 index 함수가 호출된다.
    
    # 아래 url 들은 위임시킬 것임

    # path('articles/', views.index),
    # path('dinner/', views.dinner),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('articles/<int:num>/',views.detail ),

    # 저쪽으로 보낼 path는 여전히 필요합니다.
    # 클라이언트 요청 주소가 /articles/까지 일치한다면,
    # 나머지 주소는 articles 앱의 urls.py로 넘긴다.
    path('articles/', include('articles.urls')),
]





