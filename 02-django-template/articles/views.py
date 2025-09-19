import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    pass


def search(request):
    pass


def throw(request):
    pass


def catch(request):
    pass


def detail(request):
    pass


def greeting(request):
    pass
