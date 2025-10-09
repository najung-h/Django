# articles/urls.py
from django.urls import path
from . import views # 명시적 상대경로


app_name = 'articles' # app 이름 지정
urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>/", views.detail, name="detail"),
    path('new/', views.new, name= "new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
