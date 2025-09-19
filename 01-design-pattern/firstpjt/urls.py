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
from django.urls import path
from articles import views

# 주소를 쓸 때는 path 함수를 꼭 써주어야 함.
urlpatterns = [
    path('admin/', admin.site.urls),
    #url로 articles/까지 일치 되었을 때 두 번째 인자에 있는 view 함수를 호출하게 된다.
    path('articles/', views.index),
    # 네이버의 선택 : 기본 화면도 main페이지를 띋우고 싶다면 빈문자열 
    path('', views.index) 
    # 에듀싸피의 선택 : 
    # 혹은 도메인 연결할 때 http->https 로 리디렉션 하듯이 
    # 그냥 edussafy.com 하면 edussafy.com/index.do로 연결될 수 있게끔 해놓는 것처럼
    # 서버 딴에서도 설정하는 방법이 있다! 
    # 둘 중 무언가를 설정할지는 개발자의 선택이다! ㅎ
]
