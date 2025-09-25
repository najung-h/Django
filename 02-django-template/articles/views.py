import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    context = {
        'name' : 'Jane',
    }
    # 장고 템플릿에서 저 context를 사용할 수 있게됨.
    # html이 아니라 장고 html이기 때문에 약간의 자유도가 있음.
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    context = {
        # 키랑 벨류랑 같게 해도 상관없으니까, 그냥 관례적으로 같게 설정합니다.
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)


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
