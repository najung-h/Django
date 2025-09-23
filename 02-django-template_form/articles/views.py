import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    pass


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    # 페이지만 응답하면 됨
    return render(request, 'articles/throw.html')


def catch(request):
    pass


def detail(request):
    pass


def greeting(request):
    pass
