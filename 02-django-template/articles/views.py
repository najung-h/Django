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
    return render(request,'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')

# 사용자 입력 데이터를 추출해서 응답 페이지에 보여주기
def catch(request):
    # 사용자 입력 데이터는 대체 어디에 있을까?
    # 사용자가 입력한 데이터는 모두 request라는 객체 덩어리 어딘가에 존재한다!
    # 그래서, request를 뜯어서 message를 찾아보자
    # print(request) # <WSGIRequest: GET '/catch/?message=ssafy'>
    '''WSGI 형태의 요청 객체이다. 아직 풀기 전인 객체 덩어리. 덩어리 이름인 것. 그래서 그 덩어리의 속성들이 나와있음
    그런데 보니 여기에 message = ssafy 라는 것이 들어있는거에요.
    이거 까면 엄청 크거든요?
    그래서 속성값을 찾기가 어려워요.
    '''
    # print(request.GET) # <QueryDict: {'message': ['ssafy']}>
    '''
    이제 드디어 찾을 수 있을 것 같아요.
    덩어리긴한데, 눈치껏 쓸 수 있을 것 같지 않나요.
    request > GET > 'message : [ssafy]' 이런 느낌일 것 같죠.
    딕셔너리 형태로 되어있네요.
    그런데, 우리가 준 message를 기준으로 dictionary로 되어있네요?'''
    # print(request.GET.get('message'))  # ssafy
    context = {
        'message' : request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)

# views.py
def detail(request, num):
    # 이제는 request 두 번째 인자로 variable routing 인자를 쓸 겁니다.
    # 없으면 에러고요
    # num 이라는 변수명이 키워드 인자로 바로 넘어가기 때문에, 이름이 같아야 합니다.
    # 다른 이름이면 못 받아요.
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)

def greeting(request):
    pass
