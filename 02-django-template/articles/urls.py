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

from django.urls import path
# 경로가 바뀌었음. 상대경로로 바꾸어주어야함
# 장고는 import views 보다 현재 디렉토리임을 명시해주는 것을 좋아합니다.
from . import views

# 앱의 urls.py
urlpatterns = [
    # articles/
    # path('articles/', views.index),
    # 위는 메인페이지로 사용하기 위해 메인 페이지로 쓸 거임
    path('', views.index),
    # 이제는 주소가 아무리 길어져도, name 만 기억하면 됨.
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name = 'search'),
    path('throw/', views.throw),
    path('catch/', views.catch),
    # 얘도
    # path('articles/<int:num>/',views.detail ),
    path('<int:num>/', views.detail),
]
